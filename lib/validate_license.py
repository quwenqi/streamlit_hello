import json
import hashlib
import datetime

def validate_license(license_file="license.json"):
    try:
        with open(license_file, "r") as file:
            license_data = json.load(file)

        # 提取许可证数据和哈希签名
        license_content = json.dumps(license_data["data"])
        
        expected_hash = license_data["hash"]

        # 验证哈希签名
        actual_hash = hashlib.sha256(license_content.encode()).hexdigest()

        if actual_hash != expected_hash:
            print("许可证验证失败：哈希不匹配")
            return False

        # 检查许可证是否过期
        expires_at = datetime.datetime.fromisoformat(license_data["data"]["expires_at"])
        if datetime.datetime.now() > expires_at:
            print("许可证已过期")
            return False

        print("许可证有效")
        return True

    except Exception as e:
        print(f"验证许可证时出错: {e}")
        return False

# 示例用法
validate_license()