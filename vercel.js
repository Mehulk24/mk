{
    "version"= 2,
    "builds"= [
        {
         "src": "mk/wsgi.py",
         "use": "@vercel/python",
         "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
        },
        {
         "src": "build_files.sh",
         "use": "@vercel/static-build",
         "config": {
            "distDir": "staticfiles_build"
         }
        }
    ],
    "routes"= [
        {
         "src": "/static/(.*)",
         "dest": "/static/$1"
        },
        {
         "src": "/(.*)",
         "dest": "poll/wsgi.py"
        }
    ]
}