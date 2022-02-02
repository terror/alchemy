date := `date`

default: push

push:
  git add .
  git commit -m "{{date}}"
  git push origin master

amend:
  git add .
  git commit --amend --no-edit
  git push -f origin master
