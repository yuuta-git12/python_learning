"""コンソールでユーザーにに表示する機能"""
import os
import string
import termcolor

def get_template_dir_path():
    """templatesディレクトリのパスを取得するメソッド

    Returns:
        str:templatesディレクトリのパス 
    """
    temlpate_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            temlpate_dir_path = settings.TEMPLATE_PATH
    # import文でモジュールをロードした際に問題が発生した場合に行う処理
    except ImportError:
        pass
    if not temlpate_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        temlpate_dir_path = os.path.join(base_dir, 'templates')
    return temlpate_dir_path


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """テンプレートファイルのパスを取得するメソッド

    Args:
        temp_file (_type_): テンプレートファイルが保存されているディレクトのパス

    Raises:
        NoTemplateError: テンプレートファイルが存在しない場合に読み出される例外処理

    Returns:
        str: テンプレートファイルのパス
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    # テンプレートファイルを保存したディレクトリが存在しない場合
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Cound not find {}'.format(temp_file_path))

    return temp_file_path


def get_template(template_file_path, color=None):
    """指定したテンプレートの文字列を返す

    Args:
        template_file_path (_type_): _description_
        color (_type_, optional): _description_. Defaults to None.

    Returns:
        string.Template:テンプレートの文字列
    """
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}'.format(
            contents=contents, splitter="="*60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
    
