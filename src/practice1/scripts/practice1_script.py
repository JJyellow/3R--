"""CLI script for the practice1 package. This will be called on the command line"""

import click

from practice1.practice1 import hello_world, repeat_three_times



@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.option("--repeat", is_flag=True, help="Repeat the message three times")  # 2. 新增這行開關
@click.version_option()
def practice1_cli(message, repeat):  # 3. 參數這裡多接一個 repeat
    """Example script. This function is referenced in setup.cfg"""
    # 4. 判斷如果有加 --repeat 就重複三次，沒有就照原本的執行
    if repeat:
        click.echo(repeat_three_times(message))
    else:
        click.echo(hello_world(message))
