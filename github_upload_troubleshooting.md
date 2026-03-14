# GitHub Upload Troubleshooting for `aws101`

## Goal

Upload the local `aws101/` Git repository to `https://github.com/YS-2357/aws101.git`.

## What Happened

### 1. Token was stored in `.env`

I saved a GitHub token in `aws101/.env` and expected `git push` to use it automatically.

Problem:

- `git push` does not read `.env` automatically.
- A token inside `.env` is only storage, not authentication setup.

## 2. Initial Git/GitHub checks

Local repository state was valid:

- local branch: `main`
- remote: `origin -> https://github.com/YS-2357/aws101.git`
- local commits existed

But GitHub access checks showed problems:

- at one point the repo looked missing from the token's accessible repo list
- later the repo `YS-2357/aws101` was confirmed to exist

## 3. First authenticated push attempt failed

I tried pushing with an explicit token-based Git command.

Error:

```text
remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/YS-2357/aws101.git/': The requested URL returned error: 403
```

Meaning:

- authentication format was accepted
- repository existed
- token did not have enough permission to push

## 4. Minimum permission needed

For a fine-grained personal access token, the minimum required permission was:

- Repository access: include `YS-2357/aws101`
- Repository permission: `Contents -> Read and write`

Important:

- `Contents: Read` is not enough for `git push`
- `Contents: Read and write` is required

Optional only if modifying workflow files under `.github/workflows/`:

- `Workflows -> Write`

## 5. Protecting the token locally

Because `.env` should not be committed, I added:

```gitignore
.env
```

This was added to `.gitignore`.

## 6. Remote history conflict

After auth started working, the remote already had its own `main` branch with:

- `README.md`
- remote commit: `043c125 Initial commit`

Local and remote histories were unrelated, so a normal push could not proceed safely.

## 7. Merge step

I merged the remote branch into local `main`:

```bash
git merge origin/main --allow-unrelated-histories
```

This completed cleanly and created a merge commit.

## 8. Final fix

The token permission was updated from read-only to read/write for repository contents.

After that, the push succeeded.

Successful result:

```text
To https://github.com/YS-2357/aws101.git
   043c125..d78cf1c  main -> main
branch 'main' set up to track 'origin/main'.
```

## Working Push Command

From inside `~/aws101`:

```bash
set -a
source .env
set +a

git -c credential.helper= \
  -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf 'YS-2357:%s' "$GITHUB_TOKEN" | base64 -w0)" \
  push -u origin main
```

## Lessons Learned

- `.env` does not automatically authenticate Git
- fine-grained PATs must include the target repository explicitly
- `git push` needs `Contents: Read and write`
- if remote and local histories differ, merge or rebase before pushing
- ignore `.env` to avoid leaking tokens into Git history
