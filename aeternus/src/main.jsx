import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { AuthProvider } from "react-oidc-context";

const cognitoAuthConfig = {
  authority: "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_4rVTRTB91",
  client_id: "2edgpr2d91i7rds9hejqif6nkp",
  redirect_uri: "http://localhost:5173/services/",
  response_type: "code",
  scope: "phone openid email",
};

const root = createRoot(document.getElementById("root"));

// wrap the application with AuthProvider
root.render(
  <StrictMode>
    <AuthProvider {...cognitoAuthConfig}>
      <App />
    </AuthProvider>
  </StrictMode>
);
