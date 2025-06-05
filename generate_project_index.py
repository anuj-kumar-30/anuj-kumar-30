import json
import os
from datetime import datetime

def read_projects():
    """Read projects from projects.json file"""
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: projects.json not found")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON in projects.json")
        return {}

def generate_markdown(projects):
    """Generate markdown content from projects data"""
    # Start with the header and basic structure
    content = f"""# 🚀 Project Dashboard

<div align="center">

![Project Dashboard](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=40&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&height=100&lines=AI+%26+ML+Projects)

</div>

## 📊 Project Statistics
- Total Projects: {len(projects)}
- Technologies Used: {count_technologies(projects)}
- Categories: {get_categories(projects)}

## 🔍 Filter Projects
<div style="display: flex; gap: 10px; margin: 20px 0;">
    <button onclick="filterProjects('all')" class="filter-btn">All</button>
    <button onclick="filterProjects('AI')" class="filter-btn">AI</button>
    <button onclick="filterProjects('LLM')" class="filter-btn">LLM</button>
    <button onclick="filterProjects('Web')" class="filter-btn">Web</button>
</div>

## 🎯 Projects

<div class="projects-table-container">
    <table class="projects-table">
        <thead>
            <tr>
                <th>Project</th>
                <th>Description</th>
                <th>Technologies</th>
                <th>Links</th>
            </tr>
        </thead>
        <tbody>
"""

    # Add each project to the table
    for project_name, project_data in projects.items():
        content += f"""            <tr class="project-row" data-tags="{','.join(project_data.get('Tags', []))}">
                <td>
                    <strong>{project_name}</strong>
                </td>
                <td>{project_data.get('Description', '')}</td>
                <td>
                    <div class="tech-stack">
"""
        # Add technology badges
        for tech in project_data.get('Tags', []):
            content += f"""                        <span class="tech-badge">{tech}</span>\n"""
        
        content += """                    </div>
                </td>
                <td>
                    <div class="project-links">
"""
        # Add GitHub link if available
        if 'github_link' in project_data:
            content += f"""                        <a href="{project_data['github_link']}" class="project-link">
                            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
                        </a>
                        <br>
"""
        # Add Live Demo link if available
        if 'live link' in project_data:
            content += f"""                        <a href="{project_data['live link']}" class="project-link">
                            <img src="https://img.shields.io/badge/Live_Demo-238636?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"/>
                        </a>
"""
        content += """                    </div>
                </td>
            </tr>
"""

    # Add the closing table tags
    content += """        </tbody>
    </table>
</div>

## 📝 Project Details
"""

    # Add detailed project information
    for project_name, project_data in projects.items():
        content += f"""
### {project_name}
- **Description:** {project_data.get('Description', '')}
- **Tech Stack:** {', '.join(project_data.get('Tags', []))}
- **Links:**
"""
        if 'github_link' in project_data:
            content += f"""  - [GitHub Repository]({project_data['github_link']})\n"""
        if 'live link' in project_data:
            content += f"""  - [Live Demo]({project_data['live link']})\n"""

    # Add the styling and JavaScript
    content += """
---

<style>
:root {
    color-scheme: dark;
}

body {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6;
}

h1, h2, h3 {
    color: #c9d1d9;
}

h1 {
    border-bottom: 1px solid #30363d;
    padding-bottom: 0.3em;
}

.filter-btn {
    background-color: #21262d;
    border: 1px solid #30363d;
    color: #c9d1d9;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-btn:hover {
    background-color: #30363d;
    border-color: #8b949e;
}

.projects-table-container {
    overflow-x: auto;
    margin: 20px 0;
}

.projects-table {
    width: 100%;
    border-collapse: collapse;
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
}

.projects-table th,
.projects-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #30363d;
}

.projects-table th {
    background-color: #21262d;
    color: #8b949e;
    font-weight: 600;
}

.projects-table tr:hover {
    background-color: #1c2128;
}

.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tech-badge {
    background-color: #21262d;
    color: #58A6FF;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.9em;
}

.project-links {
    display: flex;
    flex-direction: column;
    gap: 0;
    align-items: flex-start;
    padding: 5px 0;
}

.project-link {
    text-decoration: none;
    display: block;
    margin-bottom: 0;
    transition: all 0.3s ease;
}

.project-link:hover {
    opacity: 0.9;
    transform: scale(1.05);
}

.project-link img {
    height: 40px;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

a {
    color: #58A6FF;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>

<script>
function filterProjects(tag) {
    const projects = document.querySelectorAll('.project-row');
    projects.forEach(project => {
        const tags = project.getAttribute('data-tags').split(',');
        if (tag === 'all' || tags.includes(tag)) {
            project.style.display = '';
        } else {
            project.style.display = 'none';
        }
    });
}
</script>

<div align="center">

![Last Updated](https://img.shields.io/badge/Updated-{datetime.now().strftime('%Y--%m--%d')}-30363d)

</div>
"""
    return content

def count_technologies(projects):
    """Count unique technologies across all projects"""
    technologies = set()
    for project in projects.values():
        technologies.update(project.get('Tags', []))
    return len(technologies)

def get_categories(projects):
    """Get unique categories from project tags"""
    categories = set()
    for project in projects.values():
        categories.update(project.get('Tags', []))
    return ', '.join(sorted(categories))

def main():
    # Read projects
    projects = read_projects()
    
    # Generate markdown
    markdown_content = generate_markdown(projects)
    
    # Write to project_index.md
    try:
        with open('project_index.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print("Successfully generated project_index.md")
    except Exception as e:
        print(f"Error writing to project_index.md: {e}")

if __name__ == "__main__":
    main() 