#to run it: sh api.sh your_token

body='
{
   "api_name":"stock_basic",
   "token":"tokken",
   "hm":"$1",
   "params":{
      "list_stauts":"L"
   },
   "fields":"ts_code,name,area,industry,list_date"
}
'

body=$(echo $body | sed -e "s/tokken/${1}/g")

curl -H "content-type: application/json"\
  -H"Accept-Charset: utf-8"\
  -X POST\
  -d "$(echo $body | tr '\n' ' ')"\
  http://api.waditu.com
