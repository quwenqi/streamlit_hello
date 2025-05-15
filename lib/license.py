import uuid
import hashlib
import datetime
import json

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 12, 2)])

def generate_license(user_id,mac_address,expiration_days=30):
    # 创建许可证数据
    license_data = {
        "user_id": user_id,
        "mac_address": mac_address,
        "created_at": datetime.datetime.now().isoformat(sep=' '),
        "expires_at": (datetime.datetime.now() + datetime.timedelta(days=expiration_days)).isoformat(sep=' '),
    }

    # 生成许可证内容
    license_content = json.dumps(license_data)

    # 生成许可证哈希签名（使用一个简单的哈希算法）
    license_hash = hashlib.sha256(license_content.encode()).hexdigest()

    # 创建完整的许可证数据（包含哈希签名）
    complete_license_data = {
        "data": license_data,
        "hash": license_hash
    }

    # 将许可证数据保存到文件
    with open("license.json", "w") as file:
        json.dump(complete_license_data, file, indent=4)

    print("许可证已生成并保存到 license.json")

# 示例用法
mac_address = get_mac_address()
generate_license("user123",mac_address,30)