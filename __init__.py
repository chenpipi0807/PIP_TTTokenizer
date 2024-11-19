from .PIP_TTTokenizer import PIP_TTToken

NODE_CLASS_MAPPINGS = {
    "PIP_TTToken": PIP_TTToken
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PIP_TTToken": "PIP 分词器"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']