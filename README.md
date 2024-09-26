# Description

Generate professional-looking CVs easily.

![example](https://github.com/user-attachments/assets/6cef4bfe-d5a1-4eca-bb08-3d0fde28f573)

from

```yaml
sections:
- id: top
  children:
  - id: title
    p: Jonathan <span id="surname">Smith</span>
  - id: subtitle
    subtitle_class: ""
    subtitle: Soylent Engineer ⋅ Backend
    uppercase_and_big_letters: true
  - p:
      - Lorem ipsum dolor sit amet, consectetur...
- id: middle
  children:
  - id: lcol
    child_class: entry1
    children:
      -   title: Contact
          children:
          - img: location.svg
            imgclass: contact_icon
            right: AB1 2CD, Londinium, GB
          - img: email.svg
            imgclass: contact_icon
            right: john.smith@mail.gov.uk
          - img: phone.svg
            imgclass: contact_icon
            right: (+44) 0 00 00 00 00
      -   title: Skills
          children:
          - smalltitle: Programming Languages
            boxes:
            - C++
            - Python
            - Rust
          - smalltitle: Python Stack
            boxes:
....
```

# Why Use This

This is an alternative to using LaTeX.

LaTeX is better - I made this only because I couldn't run LaTeX on my laptop due to a bug.

# Prerequisites

* Font file(s) of your choice
* Python
* Python package `yaml`

# Usage

    python3 cv.py /path/to/my.yaml /path/to/output.html

Then convert the HTML to a PDF - there are many easy ways of doing this.