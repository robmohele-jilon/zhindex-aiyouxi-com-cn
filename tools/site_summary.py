import json
from typing import List, Dict

def load_site_data() -> Dict[str, object]:
    """返回站点资料的结构化数据"""
    return {
        "site_name": "爱游戏资源站",
        "url": "https://zhindex-aiyouxi.com.cn",
        "keywords": ["爱游戏", "游戏资源", "游戏资讯", "手游推荐", "游戏攻略"],
        "tags": ["游戏", "资源", "资讯", "评测"],
        "description": "提供最新游戏资讯、深度评测、热门手游推荐与实用攻略的综合游戏平台。",
        "features": [
            "每日更新游戏新闻",
            "独立游戏评测报告",
            "玩家社区互动板块",
            "资源下载与安装指引",
        ],
        "last_updated": "2025-04-01"
    }

def generate_summary(data: Dict[str, object]) -> str:
    """根据站点资料生成结构化摘要文本"""
    lines: List[str] = []
    lines.append("=" * 50)
    lines.append("站点摘要报告".center(46))
    lines.append("=" * 50)
    lines.append(f"站点名称：{data['site_name']}")
    lines.append(f"URL：{data['url']}")
    lines.append(f"核心关键词：{'、'.join(data['keywords'])}")
    lines.append(f"标签：{'、'.join(data['tags'])}")
    lines.append(f"简短说明：{data['description']}")
    lines.append("---")
    lines.append("特色功能：")
    for i, feature in enumerate(data['features'], 1):
        lines.append(f"  {i}. {feature}")
    lines.append(f"最后更新：{data['last_updated']}")
    lines.append("=" * 50)
    return "\n".join(lines)

def format_json_summary(data: Dict[str, object]) -> str:
    """返回JSON格式的摘要，便于程序读取"""
    summary = {
        "title": data['site_name'],
        "url": data['url'],
        "keywords": data['keywords'],
        "tags": data['tags'],
        "description": data['description'],
        "features": data['features'],
        "updated": data['last_updated']
    }
    return json.dumps(summary, ensure_ascii=False, indent=2)

def print_summary_report(data: Dict[str, object]) -> None:
    """控制台输出结构化摘要"""
    print("\n>>> 结构化摘要 <<<\n")
    print(generate_summary(data))
    print("\n>>> JSON 格式摘要 <<<\n")
    print(format_json_summary(data))

def main() -> None:
    """主入口：加载数据并输出摘要"""
    site_data = load_site_data()
    print_summary_report(site_data)

if __name__ == "__main__":
    main()