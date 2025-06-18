# Aeternus

Aeternus is an intelligent wedding planner web application built with React and Vite. It helps couples plan their weddings with ease, offering features like wedding theme suggestions based on Pinterest boards, a gallery, and contact forms.

## Features

- **Home**: Elegant landing page introducing the app.
- **About**: Learn about the team and the mission behind Aeternus.
- **Services**: Submit your Pinterest board link to get AI-generated wedding theme suggestions.
- **Gallery**: Meet the team with fun profile cards.
- **Contact Us**: Reach out for more information or support.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18 or newer recommended)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

### Installation

1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd aeternus```

2. Install dependencies:
   ```sh
   npm install
   # or
   yarn install```
### Running the App
- Start the development server:
   ```sh
   npm run dev
   # or
   yarn dev```

<h4>Open <a href="http://localhost:5173">http://localhost:5173</a> in your browser</h4>

- Building for Production
   ```sh
   npm run build
   # or
   yarn build```

- Preview Production Build
   ```sh
   npm run preview
   # or
   yarn preview```

## Project Structure

   ```sh
   aeternus/
      src/
         pages/         # React page components (Home, About, Services, etc.) 
         Card/          # Card component for Gallery
         css/           # CSS files for styling
         img/           # Images used in the app
         [App.jsx](http://_vscodecontentref_/0)        # Main App component
         [main.jsx](http://_vscodecontentref_/1)       # Entry point
      public/          # Static assets
      [index.html](http://_vscodecontentref_/2)       # HTML template
      [package.json](http://_vscodecontentref_/3)     # Project metadata and scripts
      [vite.config.js](http://_vscodecontentref_/4)   # Vite configuration
   ```

Aeternus integrates with both AWS Lambda, Bedrock and OpenSearch to analyze Pinterest boards and suggest wedding themes using AI. The Lambda function is located in the lambda_functions/ directory.

**For Testing: <a href="https://dza8twc2m699a.cloudfront.net/">https://dza8twc2m699a.cloudfront.net/</a>**
**Disclaimer: Due to limitations of LLM, prompts may take up to a minute to process. Thanks for waiting ❤️**

This project is for educational and hackathon purposes.

Built with ❤️ by university students for love.
