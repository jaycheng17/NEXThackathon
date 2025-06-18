import styles from './Card.module.css'

const Card = (props) => {
    return(
        <div className={styles.card}>
            <img className={styles.cardImage} src={props.imgs} alt="picture"></img>
            <h2 className={styles.cardTitle}>{props.name}</h2>
            <p className={styles.cardText}>{props.test}</p>
        </div>
    );
}

export default Card