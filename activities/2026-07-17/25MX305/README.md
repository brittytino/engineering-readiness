# Dynamic JSON Form Generator

## Overview
A dynamic JSON-driven form generator built with Next.js and React. The application renders forms based on a JSON schema, supports validation, conditional rendering, and nested form structures.

## Features
- Dynamic form generation from JSON
- Required field validation
- Age validation (18+)
- Conditional fields (e.g., Company Name shown only when Employed is checked)
- Centralized form state management
- Scalable component-based architecture

## Tech Stack
- Next.js
- React
- JavaScript

## Project Structure

```
app/
components/
  fields/
data/
utils/
```

## Architecture
- **FormRenderer**: Reads the JSON schema and manages form state.
- **FieldRenderer**: Renders the appropriate field component.
- **Field Components**: Reusable input components (Text, Number, Checkbox).
- **Utils**: Validation and conditional logic.

## Time Complexity
| Operation | Complexity |
|----------|------------|
| Form Rendering | O(n) |
| Validation | O(n) |
| Conditional Rendering | O(n) |
| Space Complexity | O(n) |

## Design Decisions
- JSON-driven rendering for flexibility.
- Reusable field components.
- Single source of truth using React state.
- Configuration-based conditional rendering.

## Future Improvements
- Support more field types.
- Async validation.
- Multi-step forms.
- Backend schema support.

## Run

```bash
npm install
npm run dev
```
