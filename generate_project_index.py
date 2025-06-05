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

## 🎯 Projects

| # | Project | Description | Technologies | Links |
|:--|:--------|:------------|:------------|:-----:|
"""
    # Add each project to the table
    for idx, (project_name, project_data) in enumerate(projects.items(), 1):
        # Create technology badges
        tech_badges = ' '.join([f"![{tech}](https://img.shields.io/badge/{tech}-58A6FF?style=flat-square&logo={tech.lower()}&logoColor=white)" for tech in project_data.get('Tags', [])])
        
        # Create links
        links = []
        if 'github_link' in project_data:
            links.append(f"[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)]({project_data['github_link']})")
        if 'live link' in project_data:
            links.append(f"[![Live Demo](https://img.shields.io/badge/Live_Demo-238636?style=flat-square&logo=streamlit&logoColor=white)]({project_data['live link']})")
        
        # Create anchor link for project name
        anchor_name = project_name.lower().replace(' ', '-')
        project_link = f"[**{project_name}**](#{anchor_name})"
        
        # Add project row
        content += f"| {idx} | {project_link} | {project_data.get('Description', '')} | {tech_badges} | {' '.join(links)} |\n"

    # Add project details section
    content += "\n## 📝 Project Details\n"
    for idx, (project_name, project_data) in enumerate(projects.items(), 1):
        # Create anchor for project details
        anchor_name = project_name.lower().replace(' ', '-')
        content += f"""
<a id="{anchor_name}"></a>
### {idx}. {project_name}
- **Description:** {project_data.get('Description', '')}
- **Tech Stack:** {', '.join(project_data.get('Tags', []))}
- **Links:**
"""
        if 'github_link' in project_data:
            content += f"""  - [GitHub Repository]({project_data['github_link']})\n"""
        if 'live link' in project_data:
            content += f"""  - [Live Demo]({project_data['live link']})\n"""

    # Add last updated badge
    content += f"""
---

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