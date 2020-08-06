curl "http://localhost:8000/comments/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "comment": {
      "user_id": "'"${USER_ID}"'",
      "post_id": "'"${POST_ID}"'",
      "body": "'"${BODY}"'"
    }
  }'

echo
