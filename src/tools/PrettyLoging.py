

class PrettyLoging:

  @staticmethod
  def robots_result_log(check_result: dict, rbts_list: dict) -> str:
    row_1 = f"(❗ Unavailable: {len(check_result.get('unavailable'))}"
    row_2 = f"| Available: {len(check_result.get('available'))} "
    row_3 = f"| Disallow {len(rbts_list.get('disallow'))} "
    row_4 = f"| Allow {len(rbts_list.get('allow'))})"

    return ''.join([row_1, row_2, row_3, row_4])

  