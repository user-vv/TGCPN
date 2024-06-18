from .base_bev_backbone import BaseBEVBackbone
from .dynamic_conv_backbone import DynamicConvBackbone
from .improve_backbone import ContextBackbone,DeepShallowRegre
from .MiniBiFPN import MiniBiFPN
# from .gcnet import Base_Bev
__all__ = {
    'BaseBEVBackbone': BaseBEVBackbone,
    'DynamicConvBackbone': DynamicConvBackbone,
    'ContextBackbone':ContextBackbone,
    'DeepShallowRegre':DeepShallowRegre,
    'MiniBiFPN':MiniBiFPN
    # 'GcNet':Base_Bev
}
