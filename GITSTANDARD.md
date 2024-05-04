<h3 align="center">Project Git Standards</h3>

<details >
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Getting Started">Getting Started</a>
      <ul>
        <li><a href="#Message Format">Message Format</a></li>
        <li><a href="#Commit Types">Commit Types</a></li>
        <li><a href="#Branch Naming">Branch Naming</a></li>
        <li><a href="#Branch Workflow">Branch Workflow</a></li>
      </ul>
    </li>
  </ol>
</details>

# 1. Message Format

## Each commit message should follow this format:

<type>: <description>
`<type>`: The type of the commit (e.g., feat, fix, docs, style, refactor, test, chore).
`<description>`: A concise description of the changes.

# 2. Commit Types
- *Commit messages are created in the present tense.*

- **feat**: A new feature implementation.
- **fix**: A bug fix.
- **docs**: Documentation-related changes.
- **style**: Formatting, whitespace, or code style changes.
- **refactor**: Code changes that do not affect the behavior.
- **test**: Adding or modifying tests.
- **chore**: Changes to the build process, dependencies, or auxiliary tools.

3. #### Example
    ```sh
    feat: Implement user authentication endpoint
    ```

## Branching Technique
# 1. Branch Naming

- **feature/**: For new feature development.
- **bugfix/**: For bug fixes.
- **hotfix/**: For critical bug fixes in production.
- **docs/**: For documentation-related changes.
- **refactor/**: For code refactoring.
- **test/**: For adding or modifying tests.
- **chore/**: For changes to the build process or other auxiliary tasks.

2. #### Example
    ```sh
    feature/user-authentication
    ```
    ```sh
    bugfix/fix-login-issue
    ```

# 3. Branch Workflow

1. #### Main Branches:
    - **main**: Main branch for production-ready code.
    - **staging**:For QA and pre-production environment.
    - **develop**: Integration branch for features.


2. #### Feature Workflow:
    1. Create a new feature branch from develop.
    2. Implement the feature.
    3. Create a pull request to merge back into develop.
    4. After testing and review, merge into develop.
    5. Periodically merge develop into main for release.



3. #### Bugfix Workflow:
    1. Create a new bugfix branch from main.
    2. Implement the fix.
    3. Create a pull request to merge back into main.
    4. After testing and review, merge into main.