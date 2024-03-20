# HTML template with a placeholder for the Vitessce configuration
html_template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Vitessce main page</title>
  </head>
  <body>
    <h1>Vitessce</h1>
    <div id="root"></div>

    <script type="importmap">
      {
        "imports": {
          "react": "https://esm.sh/react@18.2.0?dev",
          "react-dom": "https://esm.sh/react-dom@18.2.0?dev",
          "react-dom/client": "https://esm.sh/react-dom@18.2.0/client?dev",
          "vitessce": "https://unpkg.com/vitessce@latest"
        }
      }
    </script>
    <script type="module">
      import React from 'react';
      import { createRoot } from 'react-dom/client';
      import { Vitessce } from 'vitessce';

      const config = %CONFIG_JSON%;

      function MyApp() {
        return React.createElement(
          Vitessce,
          {
            height: 500,
            theme: 'light',
            config: config,
          }
        );
      }

      const container = document.getElementById('root');
      const root = createRoot(container);
      root.render(React.createElement(MyApp));
    </script>
  </body>
</html>
"""