---
title: "My First Post"
date: 2021-05-20T11:41:11+08:00
draft: true
---

# Hugo usage

## Step 1: Install Hugo 

`Homebrew` and `MacPorts`, package managers for `macOS`, can be installed from [brew.sh](https://brew.sh/) or [macports.org](https://www.macports.org/) respectively. See [install](https://gohugo.io/getting-started/installing) if you are running Windows etc.

```bash
brew install hugo
# or
port install hugo
```

To verify your new install:

```bash
hugo version
```

## Step 2: Create a New Site 

```bash
hugo new site quickstart
```

The above will create a new Hugo site in a folder named `quickstart`.

## Step 3: Add a Theme 

See [themes.gohugo.io](https://themes.gohugo.io/) for a list of themes to consider. This quickstart uses the beautiful [Ananke theme](https://themes.gohugo.io/gohugo-theme-ananke/).

First, download the theme from GitHub and add it to your site’s `themes` directory:

```bash
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```

*Note for non-git users:*

- If you do not have git installed, you can download the archive of the latest version of this theme from:https://github.com/theNewDynamic/gohugo-theme-ananke/archive/master.zip
- Extract that .zip file to get a “gohugo-theme-ananke-master” directory.
- Rename that directory to “ananke”, and move it into the “themes/” directory.

Then, add the theme to the site configuration:

```bash
echo theme = \"ananke\" >> config.toml
```

## Step 4: Add Some Content 

You can manually create content files (for example as `content/<CATEGORY>/<FILE>.<FORMAT>`) and provide metadata in them, however you can use the `new` command to do a few things for you (like add title and date):

```bash
hugo new posts/my-first-post.md
```

Edit the newly created content file if you want, it will start with something like this:

```markdown
---
title: "My First Post"
date: 2019-03-26T08:47:11+01:00
draft: true
---
```

Drafts do not get deployed; once you finish a post, update the header of the post to say `draft: false`. More info [here](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content).

## Step 5: Start the Hugo server 

Now, start the Hugo server with [drafts](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content) enabled:

<iframe src="https://asciinema.org/a/BvJBsF6egk9c163bMsObhuNXj/embed?rows=10" id="asciicast-iframe-BvJBsF6egk9c163bMsObhuNXj" name="asciicast-iframe-BvJBsF6egk9c163bMsObhuNXj" scrolling="no" allowfullscreen="true" style="overflow: hidden; margin: 0px; border: 0px; display: inline-block; width: 482px; float: none; visibility: visible; height: 195px;"></iframe>

```
▶ hugo server -D

                   | EN
+------------------+----+
  Pages            | 10
  Paginator pages  |  0
  Non-page files   |  0
  Static files     |  3
  Processed images |  0
  Aliases          |  1
  Sitemaps         |  1
  Cleaned          |  0

Total in 11 ms
Watching for changes in /Users/bep/quickstart/{content,data,layouts,static,themes}
Watching for config changes in /Users/bep/quickstart/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

**Navigate to your new site at http://localhost:1313/.**

Feel free to edit or add new content and simply refresh in browser to see changes quickly (You might need to force refresh in webbrowser, something like Ctrl-R usually works).

## Step 6: Customize the Theme 

Your new site already looks great, but you will want to tweak it a little before you release it to the public.

### Site Configuration 

Open up `config.toml` in a text editor:

```
baseURL = "https://example.org/"
languageCode = "en-us"
title = "My New Hugo Site"
theme = "ananke"
```

Replace the `title` above with something more personal. Also, if you already have a domain ready, set the `baseURL`. Note that this value is not needed when running the local development server.

**Tip:** Make the changes to the site configuration or any other file in your site while the Hugo server is running, and you will see the changes in the browser right away, though you may need to [clear your cache](https://kb.iu.edu/d/ahic).

For theme specific configuration options, see the [theme site](https://github.com/theNewDynamic/gohugo-theme-ananke).

**For further theme customization, see [Customize a Theme](https://gohugo.io/themes/customizing/).**

### Step 7: Build static pages 

It is simple. Just call:

```
hugo -D
```

Output will be in `./public/` directory by default (`-d`/`--destination` flag to change it, or set `publishdir` in the config file).


