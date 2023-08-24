from django.http import JsonResponse
import json
import logging
import datetime
import os

logger = logging.getLogger(__name__)


def sim_server(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            lora_name = jsonData["msg1"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.system('python /root/autodl-tmp/lora/removebg.py --lora='+lora_name)
            result='done'
            dic = {
                "desc": "Success",
                "lora": lora_name,
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic)
        except Exception as e:
            dic={'what':'eat shit'}
            return JsonResponse(dic)
            logger.info(e)
    else:
        return JsonResponse({"desc": "Good request"}, status=400)