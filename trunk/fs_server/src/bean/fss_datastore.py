# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-01-04
# desc: data store


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    sys.path.append("../base")
    sys.path.append("../dao")

from fss_proto_type import *
from fs_data_weblog_dao import *
from fs_data_statics_dao import *
from fs_data_fileatt_dao import *
from fs_data_danfunc_dao import *
from fs_data_fuzzhash_dao import *

class FsDataStore:
    
    @staticmethod
    def srote_data(reqJson):
        task_id = reqJson['task_id']
        dev_name = reqJson['dev_name']
        agent_id = reqJson['agent_id']
        msg_proto = reqJson['msg_protocol']
        msg_type = reqJson['msg_type']
        data = reqJson['data']

        if msg_proto != FsProtoProtoEnum.F_RESULT_UP:
            return False, "proto_emum error"

        if msg_type == FsProtoProtoType.F_DATA_WEBLOG:
            bRet, sRet = FsWebLogDao.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoProtoType.F_DATA_STATICS:
            bRet, sRet = FsStaticsDao.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoProtoType.F_DATA_FILEATT:
            bRet, sRet = FsFileAttDao.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoProtoType.F_DATA_DANFUNC:
            bRet, sRet = FsDanFuncDao.insert_node(agent_id, data)
            if not bRet: return False, sRet

        elif msg_type == FsProtoProtoType.F_DATA_FUZZHASH:
            bRet, sRet = FsFuzzHashDao.insert_node(agent_id, data)
            if not bRet: return False, sRet
        
        else:
            return False, "msg_type error"


        rspData = {
            "proto_emum": FsProtoProtoEnum.F_RESULT_DOWN,
            "proto_type": msg_type,
            "data": ""
        }

        return True, rspData


if __name__ == "__main__":

    reqJson = {
        "task_id": "123456qwertyuiop",
        "dev_name": "websrv_debain_8",
        "agent_id": 1002,
        "msg_protocol": 0x01,
        "msg_type": 0x01,
        "data": {
            "client_ip": "222.24.62.100",
            "time_local": "[12/01/2016 +8000]",
            "method": "POST",
            "url": "/user/add/userinfo.php",
            "req_body": "uid=1004&task=show",
            "referer": "/index.html"
        }
    }

    print FsDanFuncDao.insert_node(reqJson)


