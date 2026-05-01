#!/usr/bin/env python3
"""AI Tutor Installer

Detects which AI coding agents are installed on the system and
copies/links the tutor skill files to the correct locations so
each agent can use them.

Usage:
    python install.py              # Install for all detected agents
    python install.py --agent opencode  # Install for a specific agent
    python install.py --list       # List detected agents
    python install.py --uninstall  # Remove tutor skills from all agents
"""

import os
import shutil
import sys
from pathlib import Path

# ── Agent definitions ────────────────────────────────────────────────
# Each agent: (name, config_dir_relative_to_home, skill_filename, skill_content_processor)

AGENTS = {
    "opencode": {
        "name": "OpenCode",
        "skill_dir": "~/.opencode/skills/tutor",
        "source_file": "skills/tutor/SKILL.md",
    },
    "claude-code": {
        "name": "Claude Code",
        "skill_dir": "~/.claude/skills/tutor",
        "source_file": "skills/tutor/SKILL.md",
    },
    "codex": {
        "name": "OpenAI Codex CLI",
        "skill_dir": "~/.codex/skills/tutor",
        "source_file": "skills/tutor/SKILL.md",
    },
    "gemini": {
        "name": "Gemini CLI",
        "skill_dir": "~/.gemini/tools/tutor",
        "source_file": "skills/tutor/SKILL.md",
    },
}

PROJECT_ROOT = Path(__file__).resolve().parent


def detect_agents() -> dict[str, bool]:
    """Returns {agent_id: is_installed} for all known agents."""
    home = Path.home()
    clues = {
        "opencode": [
            home / ".opencode",
            home / ".config" / "opencode",
        ],
        "claude-code": [
            home / ".claude",
        ],
        "codex": [
            home / ".codex",
        ],
        "gemini": [
            home / ".gemini",
        ],
    }
    installed = {}
    for agent_id, paths in clues.items():
        installed[agent_id] = any(p.exists() for p in paths)
    return installed


def install_skill(agent_id: str, dry_run: bool = False) -> tuple[bool, str]:
    """Copy the tutor skill to an agent's skill directory."""
    if agent_id not in AGENTS:
        return False, f"Unknown agent: {agent_id}"

    agent = AGENTS[agent_id]
    skill_dir = Path(os.path.expanduser(agent["skill_dir"]))
    source = PROJECT_ROOT / agent["source_file"]

    if not source.exists():
        return False, f"Source file not found: {source}"

    if dry_run:
        return True, f"[DRY RUN] Would copy {source} → {skill_dir}/SKILL.md"

    skill_dir.mkdir(parents=True, exist_ok=True)
    dest = skill_dir / "SKILL.md"
    shutil.copy2(source, dest)

    # Also copy references/ and templates/ directories
    for subdir in ["references", "templates"]:
        src_subdir = PROJECT_ROOT / "skills" / "tutor" / subdir
        if src_subdir.exists():
            dst_subdir = skill_dir / subdir
            if dst_subdir.exists():
                shutil.rmtree(dst_subdir)
            shutil.copytree(src_subdir, dst_subdir)

    return True, f"Installed: {skill_dir}"


def uninstall_skill(agent_id: str) -> tuple[bool, str]:
    """Remove the tutor skill from an agent."""
    if agent_id not in AGENTS:
        return False, f"Unknown agent: {agent_id}"

    skill_dir = Path(os.path.expanduser(AGENTS[agent_id]["skill_dir"]))
    dest = skill_dir / "SKILL.md"

    if not dest.exists():
        return False, f"Not installed for {AGENTS[agent_id]['name']}"

    dest.unlink()
    # Remove references/ and templates/ subdirectories
    for subdir in ["references", "templates"]:
        subdir_path = skill_dir / subdir
        if subdir_path.exists():
            shutil.rmtree(subdir_path)
    # Remove empty dirs
    try:
        skill_dir.rmdir()
    except OSError:
        pass
    return True, f"Removed: {dest}"


def install_course(course_name: str = "ejemplo-ml") -> tuple[bool, str]:
    """Copy a course directory to the user's home for agent access."""
    course_src = PROJECT_ROOT / "cursos" / course_name
    if not course_src.exists():
        return False, f"Course not found: {course_name}"

    course_dest = Path.home() / ".ai-tutor" / "cursos" / course_name
    if course_dest.exists():
        shutil.rmtree(course_dest)
    shutil.copytree(course_src, course_dest)
    return True, f"Course installed: {course_dest}"


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Install AI Tutor skills for coding agents"
    )
    parser.add_argument(
        "--agent", "-a",
        choices=list(AGENTS.keys()),
        help="Install for a specific agent only",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List detected agents",
    )
    parser.add_argument(
        "--uninstall", "-u",
        action="store_true",
        help="Remove tutor skills from all/specified agents",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without doing it",
    )
    parser.add_argument(
        "--course", "-c",
        default="ejemplo-ml",
        help="Course name to install (default: ejemplo-ml)",
    )
    args = parser.parse_args()

    # --list
    if args.list:
        installed = detect_agents()
        print("\nAI Coding Agents detected on this system:\n")
        for agent_id, info in AGENTS.items():
            status = "✅ installed" if installed[agent_id] else "❌ not found"
            skill_dir = Path(os.path.expanduser(info["skill_dir"]))
            has_skill = (skill_dir / "SKILL.md").exists()
            skill_status = " (tutor skill present)" if has_skill else ""
            print(f"  {info['name']:<20} {status}{skill_status}")
        print()
        return

    # Determine which agents to act on
    if args.agent:
        targets = [args.agent]
    else:
        installed = detect_agents()
        targets = [aid for aid, is_installed in installed.items() if is_installed]

    if not targets:
        print("No supported coding agents detected on this system.")
        print("Supported agents: " + ", ".join(a["name"] for a in AGENTS.values()))
        print("\nTip: Run with --list to see which agents were checked.")
        return

    # Install or uninstall
    action = uninstall_skill if args.uninstall else install_skill
    action_name = "Uninstalling" if args.uninstall else "Installing"

    print(f"\n{action_name} AI Tutor skills...\n")

    success_count = 0
    for agent_id in targets:
        ok, msg = action(agent_id, dry_run=args.dry_run)
        symbol = "✅" if ok else "❌"
        print(f"  {symbol} {AGENTS[agent_id]['name']}: {msg}")
        if ok:
            success_count += 1

    # Also install course
    if not args.uninstall and not args.dry_run:
        ok, msg = install_course(args.course)
        symbol = "✅" if ok else "❌"
        print(f"  {symbol} Course '{args.course}': {msg}")
    elif not args.uninstall and args.dry_run:
        print(f"  ℹ️  [DRY RUN] Would install course '{args.course}' to ~/.ai-tutor/cursos/")

    print(f"\nDone. {success_count} agent(s) updated.\n")

    if not args.uninstall:
        print("Next steps:")
        print("  Start a session with your agent and say:")
        print('  "Load the tutor skill. I want to learn about machine learning."')
        print(f"  Or: \"Load the tutor skill and open cursos/{args.course}/curriculum.md\"")
        print()


if __name__ == "__main__":
    main()
