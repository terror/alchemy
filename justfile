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

go name:
  go run go/{{name}}.go

py name:
  python3 python/{{name}}.py

rs name:
  cd rust && cargo run --bin {{name}}

scm name:
  scheme --quiet < $(fd --glob {{name}}.scm)
