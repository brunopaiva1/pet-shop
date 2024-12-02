Realizar rebase:

OBS: Verificar branch (É necessário está na branch que irá realizar o rebase para main)

```
$ git checkout minha_branch
$ git pull origin main --rebase
$ git rebase main
$ git rebase --continue
$ git push origin dev --force
```

