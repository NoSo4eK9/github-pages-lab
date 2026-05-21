#!/usr/bin/env python3
"""
CyberLab Project Utilities
Python script for managing and analyzing the static website project.
"""

import os
import json
from datetime import datetime
from pathlib import Path
import re


class SiteAnalyzer:
    """Analyze the static website project."""

    def __init__(self, project_dir='.'):
        self.project_dir = Path(project_dir)
        self.stats = {}

    def analyze(self):
        """Run complete site analysis."""
        print("🔍 Analyzing CyberLab Project...\n")
        
        self.count_files()
        self.analyze_html()
        self.analyze_css()
        self.analyze_js()
        self.check_links()
        self.generate_report()

    def count_files(self):
        """Count project files by type."""
        stats = {
            'html': 0,
            'css': 0,
            'js': 0,
            'total': 0,
            'size_kb': 0
        }

        for ext, count in [('html', '*.html'), ('css', '*.css'), ('js', '*.js')]:
            files = list(self.project_dir.glob(count))
            stats[ext] = len(files)
            stats['total'] += len(files)
            stats['size_kb'] += sum(f.stat().st_size for f in files) / 1024

        self.stats['files'] = stats

    def analyze_html(self):
        """Analyze HTML files for structure."""
        html_files = list(self.project_dir.glob('*.html'))
        analysis = {
            'files': len(html_files),
            'pages': [],
            'total_elements': 0,
            'total_text_length': 0
        }

        for html_file in html_files:
            content = html_file.read_text(encoding='utf-8')
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content)
            title = title_match.group(1) if title_match else 'Unknown'

            # Count elements
            elements = len(re.findall(r'<[^/][^>]*>', content))
            text_length = len(re.sub(r'<[^>]*>', '', content))

            analysis['pages'].append({
                'filename': html_file.name,
                'title': title,
                'elements': elements,
                'text_length': text_length
            })
            
            analysis['total_elements'] += elements
            analysis['total_text_length'] += text_length

        self.stats['html'] = analysis

    def analyze_css(self):
        """Analyze CSS files."""
        css_files = list(self.project_dir.glob('*.css'))
        analysis = {
            'files': len(css_files),
            'total_rules': 0,
            'total_lines': 0,
            'variables': 0,
            'animations': 0
        }

        for css_file in css_files:
            content = css_file.read_text(encoding='utf-8')
            
            analysis['total_lines'] += len(content.splitlines())
            analysis['total_rules'] += len(re.findall(r'{[^}]*}', content))
            analysis['variables'] += len(re.findall(r'--[\w-]+:', content))
            analysis['animations'] += len(re.findall(r'@keyframes', content))

        self.stats['css'] = analysis

    def analyze_js(self):
        """Analyze JavaScript files."""
        js_files = list(self.project_dir.glob('*.js'))
        analysis = {
            'files': len(js_files),
            'classes': 0,
            'functions': 0,
            'total_lines': 0
        }

        for js_file in js_files:
            content = js_file.read_text(encoding='utf-8')
            
            analysis['total_lines'] += len(content.splitlines())
            analysis['classes'] += len(re.findall(r'class\s+\w+', content))
            analysis['functions'] += len(re.findall(r'(?:function|\w+\s*=\s*\(|\w+\s*\(\)|=>\s*|def\s+)', content))

        self.stats['js'] = analysis

    def check_links(self):
        """Check internal links."""
        links_analysis = {
            'internal': [],
            'external': [],
            'invalid': []
        }

        html_files = list(self.project_dir.glob('*.html'))
        
        for html_file in html_files:
            content = html_file.read_text(encoding='utf-8')
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            for link in links:
                if link.startswith('http'):
                    links_analysis['external'].append(link)
                elif link.startswith('#'):
                    links_analysis['internal'].append(link)
                elif link.endswith('.html'):
                    target = self.project_dir / link
                    if target.exists():
                        links_analysis['internal'].append(link)
                    else:
                        links_analysis['invalid'].append(f"{link} (from {html_file.name})")

        self.stats['links'] = links_analysis

    def generate_report(self):
        """Generate and print analysis report."""
        report = f"""
╔════════════════════════════════════════════════════════════╗
║           📊 CyberLab Project Analysis Report              ║
╚════════════════════════════════════════════════════════════╝

📁 PROJECT FILES
├─ HTML Files: {self.stats['files']['html']}
├─ CSS Files: {self.stats['files']['css']}
├─ JS Files: {self.stats['files']['js']}
├─ Total Files: {self.stats['files']['total']}
└─ Total Size: {self.stats['files']['size_kb']:.2f} KB

📄 HTML STRUCTURE
├─ Pages: {self.stats['html']['files']}
├─ Total Elements: {self.stats['html']['total_elements']}
├─ Text Content: {self.stats['html']['total_text_length']} characters
└─ Pages:
"""
        for page in self.stats['html']['pages']:
            report += f"    • {page['filename']}: {page['elements']} elements\n"

        report += f"""
🎨 CSS STYLING
├─ Stylesheets: {self.stats['css']['files']}
├─ CSS Rules: {self.stats['css']['total_rules']}
├─ CSS Variables: {self.stats['css']['variables']}
├─ Animations: {self.stats['css']['animations']}
└─ Lines of Code: {self.stats['css']['total_lines']}

⚙️  JAVASCRIPT
├─ Scripts: {self.stats['js']['files']}
├─ Classes: {self.stats['js']['classes']}
├─ Functions: {self.stats['js']['functions']}
└─ Lines of Code: {self.stats['js']['total_lines']}

🔗 LINKS ANALYSIS
├─ Internal Links: {len(self.stats['links']['internal'])}
├─ External Links: {len(self.stats['links']['external'])}
└─ Invalid Links: {len(self.stats['links']['invalid'])}
"""
        if self.stats['links']['invalid']:
            report += "⚠️  Invalid Links Found:\n"
            for link in self.stats['links']['invalid']:
                report += f"   ❌ {link}\n"

        report += f"""
✅ RECOMMENDATIONS
"""
        recommendations = self.get_recommendations()
        for i, rec in enumerate(recommendations, 1):
            report += f"{i}. {rec}\n"

        report += f"""
📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 Project: CyberLab GitHub Pages
╚════════════════════════════════════════════════════════════╝
"""
        print(report)
        return report

    def get_recommendations(self):
        """Generate optimization recommendations."""
        recommendations = []

        # Check file sizes
        if self.stats['files']['size_kb'] > 100:
            recommendations.append("📦 Consider minifying CSS and JS files (current size > 100KB)")

        # Check CSS
        if self.stats['css']['animations'] > 10:
            recommendations.append("🎬 Many animations found - monitor performance on low-end devices")

        # Check JS
        if self.stats['js']['total_lines'] > 500:
            recommendations.append("📝 Large JS file - consider splitting into modules")

        # Check links
        if self.stats['links']['invalid']:
            recommendations.append("🔗 Fix broken internal links for better user experience")

        # Default recommendations
        if not recommendations:
            recommendations = [
                "✨ Site looks great! Keep maintaining high code quality",
                "🚀 Consider adding service worker for offline support",
                "📱 Test responsiveness on mobile devices regularly"
            ]

        return recommendations

    def export_json(self, filename='report.json'):
        """Export analysis to JSON file."""
        output_file = self.project_dir / filename
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Report exported to {filename}")


class ContentGenerator:
    """Generate content for the website."""

    @staticmethod
    def generate_metadata():
        """Generate metadata for SEO."""
        metadata = {
            'title': 'CyberLab | Static Website on GitHub Pages',
            'description': 'Interactive educational project demonstrating HTML, CSS, JavaScript and GitHub Pages deployment',
            'keywords': ['GitHub Pages', 'HTML', 'CSS', 'JavaScript', 'Web Development', 'Static Website'],
            'author': 'CyberLab Team',
            'og_image': 'https://github.com/cyberlab-demo.jpg',
            'robots': 'index, follow',
            'language': 'uk'
        }
        return metadata

    @staticmethod
    def generate_sitemap():
        """Generate sitemap entries."""
        sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://cyberlab-demo.github.io/</loc>
    <lastmod>2026-05-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://cyberlab-demo.github.io/about.html</loc>
    <lastmod>2026-05-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://cyberlab-demo.github.io/projects.html</loc>
    <lastmod>2026-05-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
        return sitemap


def main():
    """Main entry point."""
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║           🚀 CyberLab Project Management Tool             ║")
    print("╚════════════════════════════════════════════════════════════╝\n")

    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'analyze':
            analyzer = SiteAnalyzer('.')
            analyzer.analyze()
            if len(sys.argv) > 2 and sys.argv[2] == '--export':
                analyzer.export_json()
        
        elif command == 'metadata':
            metadata = ContentGenerator.generate_metadata()
            print("\n📋 Generated Metadata:")
            print(json.dumps(metadata, indent=2, ensure_ascii=False))
        
        elif command == 'sitemap':
            sitemap = ContentGenerator.generate_sitemap()
            print("\n🗺️  Generated Sitemap:")
            print(sitemap)
            with open('sitemap.xml', 'w', encoding='utf-8') as f:
                f.write(sitemap)
            print("\n✅ Sitemap saved to sitemap.xml")
        
        else:
            print(f"Unknown command: {command}")
            print("\nAvailable commands:")
            print("  • python utils.py analyze        - Analyze project")
            print("  • python utils.py analyze --export - Analyze and export JSON")
            print("  • python utils.py metadata      - Generate SEO metadata")
            print("  • python utils.py sitemap       - Generate sitemap")
    else:
        analyzer = SiteAnalyzer('.')
        analyzer.analyze()


if __name__ == '__main__':
    main()
