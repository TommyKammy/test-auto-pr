# Test Auto-PR Repository

This repository demonstrates automated issue-to-PR workflow using GitHub Actions and OpenClaw.

## How it works

1. **Issue created** → GitHub Action triggers
2. **Notification sent** → OpenClaw receives webhook
3. **Analysis & Coding** → OpenClaw sub-agent analyzes the issue
4. **PR created** → Code changes submitted as pull request

## Sample Code

See `src/calculator.py` for a simple module that can be extended via issues.
