import re
from itertools import repeat


def _get_real_int_parts(num_str, num_del_pos):
    if num_str[0] == '0':
        int_num_part = None
        re_obj = re.search(r'[1-9]\d*$', num_str[2:])
        real_num_part = re_obj[0] if re_obj else ''
    else:
        int_num_part = num_str[:num_del_pos]
        real_num_part = num_str[num_del_pos + 1:]
    return int_num_part, real_num_part


def _exec_round_on_step(val, step, is_up):
    remainder = val % step
    if remainder == 0:
        return val
    res = val - remainder
    return res if not is_up else res + step


def _convert_int_str2float(int_str, int_str2, count):
    if len(int_str) > len(int_str2):
        count -= 1
    elif len(int_str) < len(int_str2):
        count += 1
    return count


def _get_del_pos_and_int_num(num_str):
    num_del_pos = num_str.find('.')
    int_num_part, real_num_part = _get_real_int_parts(num_str, num_del_pos)
    int_num_str = int_num_part + real_num_part if int_num_part else real_num_part
    return num_del_pos, int(int_num_str), int_num_str, real_num_part


def _convert_norm_float_to_float_str(num: float) -> str:
    if groups := re.match(r'^(?P<num>-?\d(.\d+)?)e-0?(?P<pow>\d+)$', str(num)):
        return '0.' + ''.join(list(repeat('0', int(groups['pow']) - 1))) + ''.join(groups['num'].split('.'))
    else:
        return str(num)


def _round_on_step(val, step, is_up=False):
    is_neg = val < 0
    if is_neg:
        is_up = not is_up
        val *= -1
    if step > val:
        if is_neg:
            step *= -1
        return step if is_up else 0
    if step % 1 == 0:
        return _exec_round_on_step(int(val), step, is_up)
    step_str = _convert_norm_float_to_float_str(step)
    val_str = _convert_norm_float_to_float_str(val)
    if isinstance(val, int):
        val_str += '.0'
    step_real_part_str = step_str.split('.')[1]
    val_real_part_str = val_str.split('.')[1]
    zeros_str = ''.join(list(repeat('0', len(step_real_part_str) - len(val_real_part_str))))
    val_str = val_str[:len(val_str.split('.')[0] + step_real_part_str) + 1] + zeros_str
    step_del_pos, int_step, _, _ = _get_del_pos_and_int_num(step_str)
    val_del_pos, int_val, int_val_str, real_val_part = _get_del_pos_and_int_num(val_str)
    int_res_str = str(_exec_round_on_step(int_val, int_step, is_up))

    if val_zeros_count := len(val_str) - len(real_val_part) - 2 if val_str[0] == '0' else None:
        val_zeros_count = _convert_int_str2float(int_res_str, int_val_str, val_zeros_count)
        res = float('0.' + ''.join(list(repeat('0', val_zeros_count))) + int_res_str)
    else:
        val_del_pos = _convert_int_str2float(int_val_str, int_res_str, val_del_pos)
        res = float(int_res_str[:val_del_pos] + '.' + int_res_str[val_del_pos:])
    return -res if is_neg else res


def ceil(val: float, step: float) -> float:
    return _round_on_step(val, step, True)


def floor(val: float, step: float) -> float:
    return _round_on_step(val, step)
