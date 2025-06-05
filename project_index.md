# 🚀 Project Dashboard

<div align="center">

![Project Dashboard](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=40&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&height=100&lines=AI+%26+ML+Projects)

</div>

## 📊 Project Statistics
- Total Projects: 2
- Technologies Used: 5
- Categories: Google AI, LLM, OpenAI, Python, streamlit

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
            <tr class="project-row" data-tags="streamlit,Python,OpenAI,LLM">
                <td>
                    <strong>Company Sales Brochure Generator</strong>
                </td>
                <td>AI-powered tool that automatically generates professional sales brochures for companies using natural language processing and customizable templates.</td>
                <td>
                    <div class="tech-stack">
                        <span class="tech-badge">streamlit</span>
                        <span class="tech-badge">Python</span>
                        <span class="tech-badge">OpenAI</span>
                        <span class="tech-badge">LLM</span>
                    </div>
                </td>
                <td>
                    <div class="project-links">
                        <a href="https://github.com/anuj-kumar-30/Company_Sales_Brochure_Generator" class="project-link">
                            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
                        </a>
                        <br>
                        <a href="https://anuj-kumar-30-company-sales-brochure--brochure-streamlit-w2huvs.streamlit.app/" class="project-link">
                            <img src="https://img.shields.io/badge/Live_Demo-238636?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"/>
                        </a>
                    </div>
                </td>
            </tr>
            <tr class="project-row" data-tags="streamlit,Python,Google AI,LLM">
                <td>
                    <strong>Chat with Multiple PDFs</strong>
                </td>
                <td>An AI-powered application that allows users to chat with multiple PDF documents simultaneously, extracting and analyzing information using Google's AI model.</td>
                <td>
                    <div class="tech-stack">
                        <span class="tech-badge">streamlit</span>
                        <span class="tech-badge">Python</span>
                        <span class="tech-badge">Google AI</span>
                        <span class="tech-badge">LLM</span>
                    </div>
                </td>
                <td>
                    <div class="project-links">
                        <a href="https://github.com/anuj-kumar-30/chat-with-multiple-pdfs/tree/main" class="project-link">
                            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
                        </a>
                        <br>
                        <a href="https://chat-with-mulitple-pdfs.streamlit.app/" class="project-link">
                            <img src="https://img.shields.io/badge/Live_Demo-238636?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"/>
                        </a>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</div>

## 📝 Project Details

### Company Sales Brochure Generator
- **Description:** AI-powered tool that automatically generates professional sales brochures for companies using natural language processing and customizable templates.
- **Tech Stack:** streamlit, Python, OpenAI, LLM
- **Links:**
  - [GitHub Repository](https://github.com/anuj-kumar-30/Company_Sales_Brochure_Generator)
  - [Live Demo](https://anuj-kumar-30-company-sales-brochure--brochure-streamlit-w2huvs.streamlit.app/)

### Chat with Multiple PDFs
- **Description:** An AI-powered application that allows users to chat with multiple PDF documents simultaneously, extracting and analyzing information using Google's AI model.
- **Tech Stack:** streamlit, Python, Google AI, LLM
- **Links:**
  - [GitHub Repository](https://github.com/anuj-kumar-30/chat-with-multiple-pdfs/tree/main)
  - [Live Demo](https://chat-with-mulitple-pdfs.streamlit.app/)

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
