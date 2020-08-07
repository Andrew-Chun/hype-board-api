curl "http://localhost:8000/users/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
