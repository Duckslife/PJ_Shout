#!/usr/bin/env bash

##############################################
# TallyBy API v1 Test Client
##############################################
# set -o nounset

LOCAL="http://localhost:8000"
AMAZON="http://a-tallyby.ddns.net"

HOST=
USER_EMAIL="interpolar.test1@gmail.com"
USER_PASSWORD="151550inter"

declare -a SAMPLE_NAME=("test1" "test2" "test3" "test4" "test5" "test6")
declare -a SAMPLE_EMAIL=("interpolar.test1@gmail.com" "interpolar.test2@gmail.com" "interpolar.test3@gmail.com" "interpolar.test4@gmail.com" "interpolar.test5@gmail.com" "interpolar.test6@gmail.com")
declare -a SAMPLE_PHONE=("010-111-1111" "010-222-2222" "010-333-3333" "010-444-4444" "010-555-5555" "010-666-6666")

function join {
  check_tool
  echo "Req> ${FUNCNAME[0]}"

  while getopts 'u:p:' OPTION; do
    case $OPTION in
      u) email=$OPTARG;;
      p) password=$OPTARG;;
    esac
  done

  local N=$(shuf -i 1-5 -n 1)
  local sample_name=$(echo "${SAMPLE_NAME[N]}")
  local sample_email=$(echo "${SAMPLE_EMAIL[N]}")
  local sample_phone=$(echo "${SAMPLE_PHONE[N]}")

  local url="/v1/users"
  printf "POST %s\n" "$HOST$url" >&2
  local json=$(curl -XPOST $HOST$url -H 'Content-Type: application/json' \
	  -d '{
  		"username": "'$sample_name'",
  		"email": "'$sample_email'",
		"password": "'$USER_PASSWORD'",
		"lat": 37.500810,
		"lng": 127.036936,
		"phone": "'$sample_phone'",
        "attr":{
            "snstype": "FaceBook",
            "accessid": "012034412",
            "email": "'$sample_email'"
        }
	  }' | json)
  echo $json
}

function users {
  check_tool
  local url="/v1/users"
  local json=$(curl -XGET $HOST$url | json)
  echo $json
}

function login {
  check_tool
  echo "Req> ${FUNCNAME[0]}"

  while getopts 'u:p:' OPTION; do
    case $OPTION in
      u) email=$OPTARG;;
      p) password=$OPTARG;;
    esac
  done

  local url="/v1/users/self/login"
  printf "GET %s\n" "$HOST$url" >&2

  local email=$([ -n "$email" ] && echo $email || echo $USER_EMAIL)
  local password=$([ -n "$password" ] && echo $password || echo $USER_PASSWORD)
  local json=$(curl -vXGET $HOST$url -d email=$email -d password=$password | json)

  echo $json
}

function logout {
  echo "Req> ${FUNCNAME[0]}"
  #TODO
}

function random_string {
  cat /dev/urandom | LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w ${1:-32} | head -n 1
}

function to_array {
  local IFS=,
  set -- $1
  for range; do
    case $range in
      *-*) for (( i=${range%-*}; i<=${range#*-}; i++ )); do echo $i; done ;;
      *)   echo $range ;;
    esac
  done
}

function usage {
  local cmd='command'
  printf 'Usage: %s <host> <command>\n' $(basename $0) >&2
  printf -- ' host may be \tlocal|smile\n' >&2
  printf -- ' command may be join|login|logout\n\n' >&2

  printf -- ' requirements: run `sudo npm install -g json`\n' >&2
  printf -- ' command: \n' >&2
  printf -- '  login -u <email> -p <password>\n' >&2
  # printf -- '  (You can omit the options in command if you want to use its default/random values)\n' >&2

  exit 2
}

function check_tool {
  local json=$(which json)
  if [ ! -x "$json" ]; then
    echo "error: json not found in ($PATH)"
    exit 2;
  fi
}

if [ $# -lt 2 ]; then
  usage $0
  exit
fi

printf '================================\n'
printf 'TallyBy API Client\n\n'

printf 'by yyoon@interpolar.co.kr\n'
printf '================================\n\n'

case "$1" in
  "local")
    HOST=$LOCAL
    CMD=$2; shift 2; $CMD $@
    ;;
  "smile")
    HOST=$SMILE
    CMD=$2; shift 2; $CMD $@
    ;;
  *) usage $0
    ;;
esac
