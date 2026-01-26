# GitHub Copilot Agent System: A Complete Guide

> **About This Guide**: This documentation explains how to work with SKILL files, instruction files, prompt files, agent files, and specs in the context of GitHub Copilot. It provides a comprehensive framework for organizing and structuring AI agent configurations to enhance your development workflow.

## Table of Contents
1. [Overview](#overview)
2. [File Types and Their Purposes](#file-types-and-their-purposes)
3. [Directory Structure](#directory-structure)
4. [Typical Use Cases](#typical-use-cases)
5. [Specs and Their Role](#specs-and-their-role)
6. [Complete Workflow](#complete-workflow)
7. [Best Practices](#best-practices)
8. [Examples](#examples)

---

## Overview

> **Note**: This guide describes the conceptual framework and best practices for organizing AI agent configurations in your repository. The file formats and structures presented here are based on GitHub Copilot's extensibility patterns and common practices for customizing AI coding assistants. While GitHub Copilot Workspace supports custom agents, the specific implementation details may vary. This guide serves as a reference architecture for structuring agent-related files in your repository.

GitHub Copilot's agent system allows you to customize and extend the behavior of AI coding agents that work on your repository. The system uses several types of files to define agent capabilities, instructions, prompts, and specifications. Understanding how these files work together is crucial for effectively leveraging Copilot's power in your development workflow.

### Key Concepts

- **SKILL files** (`.skill`): Define specialized capabilities and tools for agents
- **Instruction files**: Provide high-level directives and guidelines for agent behavior
- **Prompt files**: Contain templates and context for specific tasks
- **Agent files**: Configure custom agents with specific roles and responsibilities
- **Specs**: Define acceptance criteria and requirements for tasks

---

## File Types and Their Purposes

### 1. SKILL Files (`.skill`)

**Location**: `.github/agents/skills/`

**Purpose**: SKILL files define specialized capabilities that custom agents can use. Think of them as "superpowers" or tools that enhance an agent's ability to perform specific tasks.

**Structure**:
```yaml
name: "skill-name"
description: "What this skill does"
tools:
  - tool1
  - tool2
context: |
  Additional context about when and how to use this skill
examples:
  - example1
  - example2
```

**Key Characteristics**:
- Define reusable capabilities across multiple agents
- Can specify which tools the agent should use
- Include context about when the skill should be applied
- Can be composed to create more complex agent behaviors

**Common Use Cases**:
- Code refactoring patterns
- Testing strategies
- Documentation generation
- Security scanning procedures
- Code review guidelines

### 2. Instruction Files

**Location**: `.github/agents/instructions/`

**Purpose**: Instruction files provide high-level directives that guide agent behavior. They define how an agent should approach tasks, what standards to follow, and what constraints to respect.

**Structure**:
```markdown
# Agent Instructions

## General Guidelines
- Guideline 1
- Guideline 2

## Code Style
- Style rule 1
- Style rule 2

## Testing Requirements
- Test requirement 1
- Test requirement 2

## Documentation Standards
- Documentation standard 1
- Documentation standard 2
```

**Key Characteristics**:
- Written in natural language (usually Markdown)
- Define overarching principles and standards
- Can be general or task-specific
- Applied to agent behavior across all tasks

**Common Use Cases**:
- Coding standards and conventions
- Testing requirements
- Documentation standards
- Security policies
- Performance requirements

### 3. Prompt Files

**Location**: `.github/agents/prompts/`

**Purpose**: Prompt files contain templates and context for specific types of tasks. They help frame problems in a way that gets the best results from agents.

**Structure**:
```markdown
# Task: {task_name}

## Context
{context_description}

## Input
{input_parameters}

## Expected Output
{output_format}

## Constraints
- Constraint 1
- Constraint 2

## Examples
{example_scenarios}
```

**Key Characteristics**:
- Task-specific templating
- Include variables that can be filled in at runtime
- Provide examples of good outputs
- Define clear success criteria

**Common Use Cases**:
- Bug fix workflows
- Feature implementation templates
- Code review prompts
- Documentation update workflows
- Refactoring task templates

### 4. Agent Files

**Location**: `.github/agents/`

**Purpose**: Agent files define custom agents with specific roles, combining skills, instructions, and prompts to create specialized AI assistants for your repository.

**Structure**:
```yaml
name: "agent-name"
description: "What this agent does"
model: "model-identifier"
skills:
  - skill1
  - skill2
instructions:
  - instruction-file-1
  - instruction-file-2
prompts:
  - prompt-template-1
default_behavior:
  - behavior1
  - behavior2
triggers:
  - trigger-condition-1
```

**Key Characteristics**:
- Combine multiple skills, instructions, and prompts
- Can specify which AI model to use
- Define when the agent should be activated
- Create specialized agents for different tasks

**Common Use Cases**:
- Python code expert agent
- Documentation specialist agent
- Security audit agent
- Test automation agent
- Code review agent

---

## Directory Structure

Here's the recommended directory structure for organizing GitHub Copilot agent files:

```
.github/
├── agents/
│   ├── README.md                    # Overview of your custom agents
│   ├── python-expert.yml            # Custom Python specialist agent
│   ├── doc-writer.yml               # Documentation agent
│   ├── security-scanner.yml         # Security-focused agent
│   ├── skills/
│   │   ├── python-refactoring.skill # Python refactoring skill
│   │   ├── api-design.skill         # API design skill
│   │   ├── testing.skill            # Testing skill
│   │   └── documentation.skill      # Documentation skill
│   ├── instructions/
│   │   ├── code-style.md            # Code style guidelines
│   │   ├── testing-requirements.md  # Testing standards
│   │   ├── security-policy.md       # Security requirements
│   │   └── documentation-style.md   # Documentation standards
│   ├── prompts/
│   │   ├── bug-fix-template.md      # Bug fix workflow
│   │   ├── feature-template.md      # Feature implementation
│   │   ├── refactor-template.md     # Refactoring tasks
│   │   └── review-template.md       # Code review prompts
│   └── specs/
│       ├── acceptance-criteria.md   # General acceptance criteria
│       └── task-specs/              # Specific task specifications
│           ├── feature-001.md
│           └── bugfix-002.md
└── workflows/
    └── copilot-tasks.yml            # GitHub Actions integration
```

---

## Typical Use Cases

### Use Case 1: Creating a Python Code Expert Agent

**When to use**: You want an agent that specializes in Python code with deep knowledge of Python best practices.

**Files involved**:
1. **Agent file** (`.github/agents/python-expert.yml`):
```yaml
name: "python-expert"
description: "Expert Python developer agent"
skills:
  - python-refactoring
  - testing
  - documentation
instructions:
  - code-style
  - testing-requirements
```

2. **Skill file** (`.github/agents/skills/python-refactoring.skill`):
```yaml
name: "python-refactoring"
description: "Refactor Python code following best practices"
context: |
  Use PEP 8 standards, type hints, and modern Python features.
  Prefer dataclasses over traditional classes when appropriate.
  Use f-strings for string formatting.
```

3. **Instruction file** (`.github/agents/instructions/code-style.md`):
```markdown
# Python Code Style Guidelines
- Follow PEP 8
- Use type hints for all function signatures
- Maximum line length: 100 characters
- Use black for formatting
```

### Use Case 2: Automating Documentation Updates

**When to use**: You need to keep documentation in sync with code changes.

**Files involved**:
1. **Agent file** (`.github/agents/doc-writer.yml`)
2. **Skill file** (`.github/agents/skills/documentation.skill`)
3. **Prompt file** (`.github/agents/prompts/doc-update-template.md`)

### Use Case 3: Security-Focused Code Reviews

**When to use**: You want automatic security analysis of code changes.

**Files involved**:
1. **Agent file** (`.github/agents/security-scanner.yml`)
2. **Skill file** (`.github/agents/skills/security-analysis.skill`)
3. **Instruction file** (`.github/agents/instructions/security-policy.md`)

---

## Specs and Their Role

### What Are Specs?

**Specs** (specifications) are detailed requirements and acceptance criteria for tasks. They bridge the gap between high-level goals and concrete implementation details.

**Location**: `.github/agents/specs/` or as part of issues/PRs

### Types of Specs

1. **Task Specs**: Define requirements for specific features or fixes
2. **Acceptance Criteria**: Define when a task is considered complete
3. **Test Specs**: Define testing requirements
4. **Performance Specs**: Define performance requirements

### Spec Structure

```markdown
# Spec: [Task Name]

## Goal
What needs to be accomplished

## Requirements
- Requirement 1
- Requirement 2

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Constraints
- Constraint 1
- Constraint 2

## Test Requirements
- Test case 1
- Test case 2

## Related Files
- file1.py
- file2.py
```

### How Specs Relate to Other Files

```
Spec (What to build)
    ↓
Agent File (Who builds it)
    ↓
Skills (How to build it)
    ↓
Instructions (Standards to follow)
    ↓
Prompts (Templates for execution)
```

**Example Flow**:
1. **Spec** defines: "Add user authentication"
2. **Agent** assigned: "python-expert"
3. **Skills** used: "api-design", "security"
4. **Instructions** followed: "security-policy.md", "code-style.md"
5. **Prompt** applied: "feature-template.md"

---

## Complete Workflow

### Step-by-Step: From Issue to Implementation

```
1. Issue/Task Created
   └── Contains: Problem description, requirements
        ↓
2. Spec Defined (if not in issue)
   └── Location: .github/agents/specs/task-specs/
   └── Contains: Detailed requirements, acceptance criteria
        ↓
3. Agent Selected/Invoked
   └── Location: .github/agents/[agent-name].yml
   └── Based on: Task type, required skills
        ↓
4. Agent Loads Configuration
   ├── Skills (.github/agents/skills/)
   ├── Instructions (.github/agents/instructions/)
   └── Prompts (.github/agents/prompts/)
        ↓
5. Agent Executes Task
   └── Using: Combined context from all files
        ↓
6. Agent Produces Output
   └── Code changes, documentation, tests
        ↓
7. Validation Against Spec
   └── Check: Acceptance criteria met
        ↓
8. Review and Merge
   └── Human review or automated checks
```

### Interaction Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    GitHub Repository                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ├─ Issue/PR with Spec
                            │
                            ↓
┌─────────────────────────────────────────────────────────┐
│              GitHub Copilot Agent System                 │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐    ┌──────────────┐                  │
│  │ Agent Config │───▶│ Task Context │                  │
│  └──────────────┘    └──────────────┘                  │
│         │                    │                          │
│         ↓                    ↓                          │
│  ┌─────────────────────────────────────┐               │
│  │     Skill Loading & Composition     │               │
│  ├─────────────────────────────────────┤               │
│  │ • Load .skill files                 │               │
│  │ • Apply instructions                │               │
│  │ • Use prompt templates              │               │
│  └─────────────────────────────────────┘               │
│         │                                               │
│         ↓                                               │
│  ┌─────────────────────────────────────┐               │
│  │      Agent Execution Engine         │               │
│  ├─────────────────────────────────────┤               │
│  │ • Analyze codebase                  │               │
│  │ • Generate changes                  │               │
│  │ • Run validations                   │               │
│  └─────────────────────────────────────┘               │
│         │                                               │
└─────────┼───────────────────────────────────────────────┘
          │
          ↓
┌─────────────────────────────────────────────────────────┐
│                    Output/Changes                        │
├─────────────────────────────────────────────────────────┤
│  • Code modifications                                    │
│  • Tests added/updated                                   │
│  • Documentation updated                                 │
│  • Validation report                                     │
└─────────────────────────────────────────────────────────┘
```

---

## Best Practices

### 1. Organizing Files

- **Keep skills atomic**: Each skill should do one thing well
- **Make instructions clear**: Use simple, direct language
- **Create reusable prompts**: Design templates that work for multiple scenarios
- **Version your specs**: Include version numbers and update dates

### 2. Naming Conventions

```
# Skills
[domain]-[action].skill
Examples: python-refactoring.skill, api-design.skill

# Instructions
[aspect]-[type].md
Examples: code-style.md, security-policy.md

# Prompts
[task-type]-template.md
Examples: bug-fix-template.md, feature-template.md

# Agents
[role]-[specialty].yml
Examples: python-expert.yml, doc-writer.yml
```

### 3. Documentation

- **Always include README.md** in `.github/agents/` explaining your custom agents
- **Document each skill**: Include examples of when to use it
- **Keep instructions updated**: Review and update regularly
- **Version your agents**: Track changes to agent configurations

### 4. Testing and Validation

- **Test agents iteratively**: Start with simple tasks
- **Validate outputs**: Ensure agents follow specifications
- **Collect feedback**: Learn from agent successes and failures
- **Refine over time**: Continuously improve skills and instructions

### 5. Security Considerations

- **Review agent access**: Limit what agents can modify
- **Audit agent actions**: Track what changes agents make
- **Sensitive data**: Never include secrets in agent files
- **Code review**: Always review agent-generated code

---

## Examples

### Example 1: Complete Python Expert Agent Setup

#### `.github/agents/python-expert.yml`
```yaml
name: "python-expert"
description: "Expert Python developer specialized in clean, maintainable code"
model: "gpt-4"
skills:
  - python-refactoring
  - type-checking
  - testing
  - documentation
instructions:
  - python-style-guide
  - testing-requirements
  - documentation-standards
default_behavior:
  - "Always add type hints"
  - "Write comprehensive docstrings"
  - "Include unit tests for new functions"
  - "Follow PEP 8 conventions"
```

#### `.github/agents/skills/python-refactoring.skill`
```yaml
name: "python-refactoring"
description: "Refactor Python code for improved readability and maintainability"
tools:
  - ast-parser
  - code-formatter
  - complexity-analyzer
context: |
  When refactoring Python code:
  1. Use type hints for all function signatures
  2. Replace string formatting with f-strings
  3. Use dataclasses for simple data containers
  4. Apply list/dict comprehensions where appropriate
  5. Follow the single responsibility principle
  6. Keep cyclomatic complexity below 10
examples:
  - "Convert traditional classes to dataclasses"
  - "Simplify nested conditionals"
  - "Extract methods from long functions"
```

#### `.github/agents/instructions/python-style-guide.md`
```markdown
# Python Style Guide

## Code Formatting
- Use Black for automatic formatting
- Maximum line length: 100 characters
- Use 4 spaces for indentation (no tabs)

## Type Hints
- All function parameters must have type hints
- All function return types must be specified
- Use `typing` module for complex types

## Naming Conventions
- Classes: PascalCase
- Functions/methods: snake_case
- Constants: UPPER_SNAKE_CASE
- Private attributes: _leading_underscore

## Imports
- Group imports: standard library, third-party, local
- Use absolute imports
- One import per line

## Docstrings
- Use Google-style docstrings
- Include: description, Args, Returns, Raises
- Add examples for complex functions
```

### Example 2: Bug Fix Workflow

#### `.github/agents/prompts/bug-fix-template.md`
```markdown
# Bug Fix Workflow

## Bug Information
- **Bug ID**: {bug_id}
- **Title**: {bug_title}
- **Severity**: {severity}
- **Reporter**: {reporter}

## Problem Description
{problem_description}

## Steps to Reproduce
1. {step_1}
2. {step_2}
3. {step_3}

## Expected Behavior
{expected_behavior}

## Actual Behavior
{actual_behavior}

## Root Cause Analysis
{root_cause}

## Solution Approach
{solution_approach}

## Implementation Checklist
- [ ] Identify the root cause
- [ ] Write a failing test that reproduces the bug
- [ ] Implement the fix
- [ ] Verify the test now passes
- [ ] Check for similar issues in the codebase
- [ ] Update documentation if needed
- [ ] Add regression test

## Testing Strategy
{testing_strategy}

## Files to Modify
- {file_1}
- {file_2}

## Related Issues
- {related_issue_1}
- {related_issue_2}
```

### Example 3: Spec for a New Feature

#### `.github/agents/specs/task-specs/add-user-authentication.md`
```markdown
# Spec: Add User Authentication

## Goal
Implement user authentication system with email/password login

## Requirements
1. User registration with email and password
2. Secure password storage (bcrypt hashing)
3. Login endpoint with JWT token generation
4. Token validation middleware
5. Logout functionality
6. Password reset flow

## Acceptance Criteria
- [ ] Users can register with email and password
- [ ] Passwords are hashed using bcrypt
- [ ] Users can log in and receive JWT token
- [ ] Protected routes verify JWT tokens
- [ ] Users can log out (token invalidation)
- [ ] Password reset email can be requested
- [ ] Passwords can be reset with valid token
- [ ] All endpoints return appropriate error messages
- [ ] Unit tests cover all endpoints
- [ ] Integration tests verify complete flows

## Constraints
- Use JWT for stateless authentication
- Token expiration: 24 hours
- Password minimum length: 8 characters
- Rate limiting: 5 login attempts per minute
- HTTPS required for production

## Security Requirements
- Never log passwords
- Use bcrypt with cost factor 12
- Validate email format
- Sanitize all inputs
- Implement CSRF protection
- Use secure HTTP-only cookies for tokens

## Test Requirements
- Unit tests for all authentication functions
- Integration tests for complete auth flows
- Security tests for common vulnerabilities
- Performance tests for login endpoint

## Related Files
- `src/auth/routes.py` (new)
- `src/auth/models.py` (new)
- `src/auth/services.py` (new)
- `src/middleware/auth.py` (new)
- `tests/test_auth.py` (new)

## API Endpoints
- POST `/api/auth/register`
- POST `/api/auth/login`
- POST `/api/auth/logout`
- POST `/api/auth/forgot-password`
- POST `/api/auth/reset-password`
- GET `/api/auth/verify` (verify token)

## Dependencies
- PyJWT for JWT tokens
- bcrypt for password hashing
- email-validator for email validation
```

---

## Summary

Understanding GitHub Copilot's agent system requires knowing how these components work together:

1. **SKILL files** provide capabilities
2. **Instruction files** set standards and guidelines
3. **Prompt files** template specific tasks
4. **Agent files** combine everything into specialized assistants
5. **Specs** define what needs to be built

The workflow flows from **specs** (what to build) through **agents** (who builds) using **skills** (how to build) while following **instructions** (standards) and **prompts** (templates).

By organizing these files properly and understanding their relationships, you can create powerful custom agents that significantly enhance your development workflow.

---

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Actions for Copilot](https://docs.github.com/en/actions)
- [Best Practices for AI-Assisted Development](https://github.blog)

---

*Last updated: January 2026*
