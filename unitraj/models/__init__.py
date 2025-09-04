from models.mtr.MTR import MotionTransformer
from models.autobot.autobot import AutoBotEgo
# from models.wayformer.wayformer import Wayformer
# from models.smart.smart import SMART

__all__ = {
    'MTR': MotionTransformer,
    'autobot': AutoBotEgo,
    # 'wayformer': Wayformer,
    # 'SMART': SMART,
}


def build_model(config):
    model = __all__[config.method.model_name](
        config=config
    )

    return model
