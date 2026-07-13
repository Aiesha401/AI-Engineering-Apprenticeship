# Day 3

## What did I build?

Today I initialized my first Git repository, made my first commit, created my first GitHub repository, and successfully pushed my local AI Engineering project to GitHub. My project now has proper version control and is available online.

## What did I learn?

- What Git is and why developers use it.
- Difference between Git and GitHub.
- How Git tracks changes in a project.
- What `git init`, `git add`, `git commit`, and `git push` do.
- What staging means before committing.
- Why `.gitignore` is important for hiding files like `.env` and `venv`.
- Difference between a local repository and a remote repository.
- How to connect a local repository to GitHub using `origin`.
- How Git authentication works and why it failed initially because of cached credentials.

## Biggest challenge today

My biggest challenge was pushing my project to GitHub. I kept getting a 403 Permission Denied error, and I didn't understand why Git was trying to use another GitHub account instead of mine.

## How did I solve it?

With my mentor's help, I checked the Git remote, found that Windows had stored old GitHub credentials, removed them, signed in again through the browser, and then pushed the project successfully. After that, my repository appeared on GitHub.

## What surprised me?

I was surprised that Git only starts tracking files after running `git add`, and that GitHub doesn't automatically know about my project until I push it. I was also surprised that Windows can save GitHub credentials and use them automatically, which caused my authentication issue.

## One thing I still don't understand

I still want to understand Git more deeply, especially what happens inside the `.git` folder and how Git stores the complete history of my project without saving full copies every time.