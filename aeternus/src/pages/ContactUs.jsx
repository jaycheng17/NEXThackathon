import '../css/ContactUs.css'

const ContactUs = () => {
  return (
    <div id="contactUsDiv">
      <form>
        <p id='header'>Get in Touch</p>
        <div className='contacts'>
          Name:
          <input type="text"/>
           Email:
          <input type="text" name="" id="" />
          Phone:
          <input type="text" name="" id="" />
          Your Message:
          <textarea name="" id=""></textarea>
        </div>
        <button type="submit" id='submitBtn'>Submit</button>
        <p id='note'>We will get back to you as soon as possible.</p>
      </form>
    </div>

);
};

export default ContactUs;