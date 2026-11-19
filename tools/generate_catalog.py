#!/usr/bin/env python3
"""Rebuild CATALOG.md from Skill frontmatter using only the Python standard library."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ("technical-content", "技术内容表达"),
    ("academic-writing", "学术成果"),
    ("research", "科研工作流"),
    ("software-engineering", "软件工程"),
]


def frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter: {path}")
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and key in ("name", "description"):
            fields[key] = value.strip().strip('"').strip("'")
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"Missing name or description: {path}")
    return fields["name"], fields["description"]


def generate() -> str:
    parts = [
        "# SkillHub Skills 索引",
        "",
        "根据当前任务选择最相关的 Skill，先读取 `SKILL.md`，再按需读取参考资料；不用一次加载全部 Skills。与每项 Skill 同名的 `RESEARCH.md` 解释方法形成的依据。",
        "",
    ]
    total = 0
    skill_categories = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    research_categories = {p.name for p in (ROOT / "research").iterdir() if p.is_dir()}
    expected_categories = {name for name, _ in CATEGORIES}
    if skill_categories != expected_categories or research_categories != expected_categories:
        raise ValueError(f"Category mismatch: skills={skill_categories}, research={research_categories}")
    for category, label in CATEGORIES:
        skills = ROOT / "skills" / category
        research = ROOT / "research" / category
        names = sorted(p.name for p in skills.iterdir() if p.is_dir())
        rnames = sorted(p.name for p in research.iterdir() if p.is_dir())
        if not names or names != rnames:
            raise ValueError(f"Missing/mismatched research directories: {category}: {names} vs {rnames}")
        parts.extend((f"## {label}（`{category}`）", "", "| Skill | 适用任务与触发说明 | 指令 | 研究依据 |", "| --- | --- | --- | --- |"))
        for name in names:
            directory = skills / name
            skill = directory / "SKILL.md"
            study = research / name / "RESEARCH.md"
            if not skill.is_file() or not study.is_file():
                raise ValueError(f"Missing Skill/research entrypoint: {category}/{name}")
            if not (directory / "agents" / "openai.yaml").is_file():
                raise ValueError(f"Missing agent metadata: {category}/{name}")
            front_name, desc = frontmatter(skill)
            if front_name != name:
                raise ValueError(f"Skill frontmatter name mismatch: {category}/{name} -> {front_name}")
            desc = desc.replace("|", "\\|").replace("\n", " ")
            parts.append(f"| `{name}` | {desc} | [SKILL.md](skills/{category}/{name}/SKILL.md) | [RESEARCH.md](research/{category}/{name}/RESEARCH.md) |")
            total += 1
        parts.append("")
    parts.extend((f"共 **{total}** 项 Skill。", "", "如需安装，请将完整 Skill 目录（包括 `references/` 等配套文件）放入目标 Agent 支持的 Skills 位置。如何通过常驻规则按需发现本索引，参见 [config/AGENTS.md](config/AGENTS.md)。", ""))
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check that CATALOG.md is current")
    args = parser.parse_args()
    content = generate()
    dest = ROOT / "CATALOG.md"
    if args.check:
        if not dest.is_file() or dest.read_text(encoding="utf-8") != content:
            print("CATALOG.md is not current; run tools/generate_catalog.py", file=sys.stderr)
            return 1
        print("CATALOG.md is up to date.")
    else:
        dest.write_text(content, encoding="utf-8")
        print("Wrote", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
