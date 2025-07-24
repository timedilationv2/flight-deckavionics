def define_env(env):
    @env.macro
    def callout(title, body):
        return f'!!! info "{title}"\n    {body}'
