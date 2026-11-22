import os

os.spawnl(mode, path)
os.spawnle(mode, path, env)
os.spawnlp(mode, file)
os.spawnlpe(mode, file, env)
os.spawnv(mode, path, args)
os.spawnve(mode, path, args, env)
os.spawnvp(mode, file, args)
os.spawnvpe(mode, file, args, env)

os.spawnl(mode, "gcc")
os.spawnle(mode, "/bin/gcc", env)
os.spawnlp(mode, "gcc")
os.spawnlpe(mode, "/bin/gcc", env)
os.spawnv(mode, "gcc", args)
os.spawnve(mode, "/bin/gcc", args, env)
os.spawnvp(mode, "gcc", args)
os.spawnvpe(mode, "/bin/gcc", args, env)
