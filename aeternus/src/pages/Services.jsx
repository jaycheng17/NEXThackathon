import { useAuth } from "react-oidc-context";
import "../css/Services.css";

function Services() {
  const auth = useAuth();

  const signOutRedirect = () => {
    const clientId = "2edgpr2d91i7rds9hejqif6nkp";
    const logoutUri = "http://localhost:5173/";
    const cognitoDomain = "https://us-west-24rvtrtb91.auth.us-west-2.amazoncognito.com";
    window.location.href = `${cognitoDomain}/logout?client_id=${clientId}&logout_uri=${encodeURIComponent(logoutUri)}`;
  };

  if (auth.isLoading) {
    return (<div className="loader-container">
      <span class="loader"></span>
    </div>);
  }

  if (auth.error) {
    return (
      <div className="errordiv">
        <p>Error: {auth.error.message}</p>
        <button className="signbtn" onClick={() => auth.signinRedirect()}>Retry Sign in</button>
      </div>
    );
  }

  if (auth.isAuthenticated) {
    return (
      <div>
        <pre> Hello: {auth.user?.profile.email} </pre>
        

        <div className="logoutdiv">
          <button className="signbtn" onClick={() => {auth.removeUser(); signOutRedirect();}}>Sign out</button>
        </div>
      </div>
    );
  }

  return (
    <div className="logindiv">
      <button className="signbtn" onClick={() => auth.signinRedirect()}>Sign in</button>
    </div>
  );
}

export default Services;