# Omnia Platform Documentation Agent Instructions

## Overview
This document provides comprehensive instructions for AI agents tasked with analyzing, documenting, and maintaining the Omnia platform codebase. The Omnia platform follows a complex, distributed multi-module architecture that requires systematic analysis approaches to ensure complete and accurate documentation.

## Core Behavioral Guidelines

### Documentation Agent Restrictions
**CRITICAL: Documentation agents MUST NOT modify the codebase under any circumstances.**

- **ALLOWED**: Create and edit **only** `.rst` files OmniaDocsG2 directories.
  - **ALLOWED**: only edit files in `./OmniaDocsG2/*` directories


- **PROHIBITED**: Any modification to:
  - make any changes to files in `./OmniaMono/*` directories
  - Source code files (`.cs`, `.ts`, `.tsx`, `.js`, etc.)
  - Configuration files (`package.json`, `*.config`, etc.)
  - Build files, manifests, or deployment scripts
  - Any file outside the designated Documentation directories

- **PURPOSE**: Documentation agents analyze and document existing code without altering it. Code modifications require separate development agents with appropriate permissions.

### Documentation Approach
- **Base documentation primarily on code analysis** using source code in ./OmniaMono/* directories
  - **secondarily on existing online documentation** from https://omnia-docs-g2.readthedocs.io/en/latest/
  - **NEVER assume** documentation is complete or accurate without code verification
- **Follow established format patterns** from existing documentation (e.g., banner.md structure)
- **Provide complete, runnable solutions** for code generation tasks
- **Include comprehensive troubleshooting** and best practices sections
- **Cross-reference related documentation** to create a cohesive knowledge base
- **Usecase examples** to illustrate concepts and guide users
- **Maintain consistency** with existing documentation style and terminology

### Code Analysis Methodology
- **Gather context first**, then perform tasks - never make assumptions
- **Use appropriate tools** systematically to collect necessary information
- **Verify file paths, APIs, and commands** before acting
- **Prefer large meaningful chunks** over small sections when reading files
- **Validate changes** with relevant build/tests/linters after substantive edits 
- **Apply the Multi-Module Architecture Analysis Protocol** for features that may be distributed across multiple modules

### Security and Best Practices
- **Never exfiltrate secrets** or make unauthorized network calls
- **Follow project package managers** and configuration standards
- **Add/update tests** when changing public behavior
- **Use minimal, pinned, widely-used libraries** for dependencies
- **Apply green-before-done validation** - run tests after changes
- **Document any assumptions** made during analysis or documentation
- **Flag incomplete information** or analysis limitations clearly in prompts and documentation
- **Maintain a clear separation** between documentation and development activities to ensure the integrity of the codebase and the reliability of the documentation.
- 

## Multi-Module Architecture Analysis Protocol

### Context
When analyzing Omnia platform features, especially those involving user interface components, action handlers, or extensible systems, the codebase follows a **distributed multi-module architecture** where functionality is split across server-side models, client-side constants, manifest registrations, and implementation directories.

### Required Analysis Steps

#### 1. Server-Side Model Investigation
- Start with C# model files (`.cs`) in `Models/` directories
- Identify base classes, enums, and static collections (e.g., `BuiltInActionButtonHandlers`)
- Note any `HandlerManifestId` or registration references

#### 2. Client-Side Constants Discovery
- **MANDATORY**: Check TypeScript constants files in **ALL** relevant modules:
  - `src/webcontentmanagement/*/app/fx/constants.ts`
  - `src/managementsystem/*/app/fx/constants.ts`
  - `src/workplace/*/app/fx/models/Constants.ts`
  - `src/*/Omnia.*.Web.Client*/app/fx/constants.ts`
- Look for `BuiltInActionButtonHandlers`, `BuiltInHandlers`, or similar collections
- Compare server-side vs client-side definitions for completeness

#### 3. Manifest Registration Analysis
- Examine `*.manifest.ts` files in `actionhandlers/` directories
- Look for `.extendApi(api => api.fx.ux.actions.handlers.configure(...))` calls
- Identify which handlers are actually registered and available

#### 4. Implementation Directory Exploration
- **MANDATORY**: Check `actionhandlers/` directories in ALL client modules
- Verify each handler has corresponding implementation files:
  - `HandlerName.manifest.ts`
  - `HandlerNameClickHandler.ts`
  - `HandlerNameSettings.tsx` (if applicable)
- Cross-reference with constants to ensure all defined handlers are implemented

#### 5. Module Coverage Verification
- **NEVER** assume a single module contains all functionality
- **ALWAYS** check WCM, Management System, and Workplace modules
- Look for feature flags or conditional loading (`.loadIfFeatureActivated`)

#### 6. Cross-Reference Validation
- Match GUIDs between server models and client constants
- Ensure manifest registrations reference correct handler IDs
- Verify no handlers are defined but not registered

### Red Flags Indicating Incomplete Analysis
- Server-side models show fewer items than client-side constants
- Implementation directories exist but aren't examined
- Manifest files reference handlers not found in initial search
- Online documentation mentions features not found in analyzed code

## Documentation Standards

### Structure and Format
- **Follow established patterns** from existing documentation (banner.md format)
- **Include comprehensive sections**:
  - Overview with clear purpose description
  - Use cases with practical examples
  - Quick start with step-by-step setup
  - Settings configuration details
  - Editor interface documentation
  - Behavior notes and limitations
  - Authoring checklists
  - Best practices
  - Troubleshooting guides
  - Related documentation links

### Block Documentation Rules
When documenting blocks, **always include the primary usage context**:
- **Page Type Usage**: Blocks typically configured once in the page type template (e.g., Breadcrumb, Navigation, Headers/Footers) that apply to all pages of that type
- **Page-Level Usage**: Blocks typically added or managed per individual page (e.g., Content blocks, Call-to-action blocks, Page-specific rollups)
- Include this context in the "Quick start" section or "Behavior notes" to guide authors on best practice placement

### File Analysis and Code Review
Before writing documentation, thoroughly review the actual implementation:
- **Check block settings UI/Style tabs** - Don't assume settings don't exist; check the actual block configuration component (Settings.tsx files)
- **Read C# models and enums** - Don't assume settings exist that aren't in the code
- **Check client-side rendering** - Review TypeScript/TSX files for actual UI behavior
- **Verify configuration options** - Ensure documented settings match what's actually configurable in the UI
- **Test against code logic** - When describing behavior, verify it matches the implementation logic
- **Document exceptions and special cases** - Note when behavior differs in specific modes (print, preview, edit, etc.)

### Behavior Documentation Accuracy
When documenting block or feature behavior:
- **Describe only configurable variations** - Don't describe behavior as changeable if there's no setting to change it
- **Distinguish between defaults and overridable behavior** - Clearly state what is default vs what can be customized
- **Include mode-specific behavior** - Note when behavior changes in print mode, preview mode, or design mode
- **Cross-reference implementation** - For complex behavior, verify against the actual rendering code
- **Flag uncertain information** - If implementation is unclear, note this rather than guessing
- **Be specific and actionable** - avoid vague descriptions
- **Include implementation evidence** from code analysis
- **Note architectural findings** and distributed system aspects
- **Flag incomplete analysis** when multi-module nature prevents full coverage
- **Use proper Markdown formatting** with consistent styling

### Technical Accuracy
- **Verify all claims** against actual code implementations
- **Cross-reference multiple sources** (server models, client constants, manifests)
- **Include version context** and dates where relevant
- **Document limitations** and known issues from code analysis

## Task Execution Guidelines

### Documentation Agent Scope
**Documentation agents are analysis and documentation specialists - NOT code modification agents.**

#### Permitted Actions:
- **Read and analyze** any file in the codebase for documentation purposes
- **Create new `.md` files** in designated Documentation directories
- **Edit existing `.md` files** in designated Documentation directories
- **Use search and analysis tools** to understand code functionality
- **Generate documentation** based on code analysis

#### Prohibited Actions:
- **NEVER modify source code** (`.cs`, `.ts`, `.tsx`, `.js`, etc.)
- **NEVER edit configuration files** (`package.json`, `*.config`, etc.)
- **NEVER change build or deployment files**
- **NEVER create or modify files outside Documentation directories**
- **NEVER execute code changes** or implement features

### Research and Analysis Tasks
- **Use systematic search patterns** - combine semantic search, grep, and file exploration
- **Follow implementation trails** from models → constants → manifests → handlers
- **Document analysis scope** clearly (which modules/files examined)
- **Apply the Multi-Module Architecture Analysis Protocol** for extensible systems

### Code Generation Tasks
- **Provide complete solutions** with all necessary files
- **Include runner/test harnesses** for validation
- **Add dependency manifests** (package.json, requirements.txt, etc.)
- **Follow project conventions** and existing code patterns

### File Editing Tasks
- **Include 3-5 lines of context** before and after changes for unambiguous targeting
- **Validate changes** with build/test runs where applicable
- **Prefer atomic changes** over large batch edits
- **Test functionality** after modifications

## Quality Assurance

### Validation Checklist
- [ ] All claims verified against actual code implementations
- [ ] Multi-module analysis completed for extensible features
- [ ] Cross-references validated between server/client code
- [ ] Documentation follows established format patterns
- [ ] Troubleshooting and best practices included
- [ ] Related documentation links provided
- [ ] Analysis scope clearly documented
- [ ] **NO CODE MODIFICATIONS MADE** - only `.md` files in Documentation directories edited

### Error Prevention
- **Never assume single-module coverage** for platform features
- **Always check client-side constants** in addition to server models
- **Verify manifest registrations** for feature availability
- **Cross-reference GUIDs and identifiers** across modules
- **Document analysis limitations** when full coverage isn't possible

## Application Scope

**Documentation agents are strictly limited to creating and editing Markdown documentation files. They must never modify source code, configuration files, or any other codebase elements.**

Apply these instructions to:
- **Documentation creation** for Omnia platform features
- **Code analysis** of distributed systems
- **Architecture documentation** and pattern identification
- **Feature implementation** and validation
- **Troubleshooting guides** and best practices
- **Migration and upgrade documentation**

## Final Directive
**Documentation agents exist solely to analyze existing code and create documentation. They MUST NOT alter the codebase in any way. Code modifications require separate development agents with explicit authorization.**

This instruction set ensures consistent, comprehensive, and accurate documentation of the Omnia platform's complex distributed architecture while maintaining strict separation between documentation and development activities.
