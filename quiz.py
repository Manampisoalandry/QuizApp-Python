def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    for question in questions:
        answer = input(question[0])
        if answer.lower() == question[1].lower():
            score += 1
    score_total = score
    score_percent = (score/10)*100
    print("Vous avez obtenu", score_total, "sur", total_questions, "questions correctes.")
    print("Vous avez obtenu", 1score_percent , " % de scores .")
    if score_percent >= 90:
        print("Félicitations, Vous etes vraiment fort(e)")
    elif score_percent >= 50:
        print("Moyen, mais pas mal")
    else :
        print("Encore plus d'effort, mais pas grave")
    return score, total_questions

def create_questions_fr():
    return [
        ("Qu'est-ce que HTML signifie ?\n(a) Hyper Text Markup Language\n(b) High Tech Multi Language\n(c) Hyperlinks and Text Markup Language\n", "a"),
        ("Quel protocole est utilisé pour envoyer des e-mails ?\n(a) SMTP\n(b) HTTP\n(c) FTP\n", "a"),
        ("Quelle est la différence entre 'git merge' et 'git rebase' ?\n(a) Aucune, ils font la même chose\n(b) 'git merge' fusionne les branches, tandis que 'git rebase' réapplique les commits\n(c) 'git rebase' fusionne les branches, tandis que 'git merge' réapplique les commits\n", "b"),
        ("Qu'est-ce qu'un réseau local (LAN) ?\n(a) Un réseau qui connecte des ordinateurs sur de longues distances\n(b) Un réseau qui connecte des ordinateurs dans une zone géographique limitée\n(c) Un réseau qui connecte des ordinateurs via Internet\n", "b"),
        ("Quel langage de programmation est souvent utilisé pour les applications Android ?\n(a) Java\n(b) Python\n(c) C#\n", "a"),
        ("Qu'est-ce que CSS signifie ?\n(a) Creative Style Sheets\n(b) Cascading Style Sheets\n(c) Computer Style Sheets\n", "b"),
        ("Quelle est la fonction principale d'un firewall ?\n(a) Protéger contre les virus\n(b) Protéger contre les attaques de sécurité\n(c) Améliorer les performances du réseau\n", "b"),
        ("Quel est le rôle du protocole DHCP dans un réseau ?\n(a) Attribution dynamique des adresses IP\n(b) Transfert de fichiers\n(c) Routage des paquets\n", "a"),
        ("Qu'est-ce que le cloud computing ?\n(a) Un réseau informatique privé\n(b) L'utilisation de serveurs distants via Internet pour stocker, gérer et traiter des données\n(c) Un protocole de sécurité pour les transactions en ligne\n", "b"),
        ("Quel est le langage de programmation le plus utilisé pour le développement web côté serveur ?\n(a) JavaScript\n(b) PHP\n(c) Ruby\n", "b")
    ]

def create_questions_en():
    return [
        ("What does HTML stand for?\n(a) Hyper Text Markup Language\n(b) High Tech Multi Language\n(c) Hyperlinks and Text Markup Language\n", "a"),
        ("Which protocol is used to send emails?\n(a) SMTP\n(b) HTTP\n(c) FTP\n", "a"),
        ("What is the difference between 'git merge' and 'git rebase'?\n(a) None, they do the same thing\n(b) 'git merge' merges branches, while 'git rebase' reapplies commits\n(c) 'git rebase' merges branches, while 'git merge' reapplies commits\n", "b"),
        ("What is a Local Area Network (LAN)?\n(a) A network that connects computers over long distances\n(b) A network that connects computers in a limited geographic area\n(c) A network that connects computers via the Internet\n", "b"),
        ("Which programming language is commonly used for Android applications?\n(a) Java\n(b) Python\n(c) C#\n", "a"),
        ("What does CSS stand for?\n(a) Creative Style Sheets\n(b) Cascading Style Sheets\n(c) Computer Style Sheets\n", "b"),
        ("What is the main function of a firewall?\n(a) Protect against viruses\n(b) Protect against security attacks\n(c) Improve network performance\n", "b"),
        ("What is the role of the DHCP protocol in a network?\n(a) Dynamic assignment of IP addresses\n(b) File transfer\n(c) Packet routing\n", "a"),
        ("What is cloud computing?\n(a) A private computer network\n(b) The use of remote servers via the Internet to store, manage, and process data\n(c) A security protocol for online transactions\n", "b"),
        ("What is the most commonly used programming language for server-side web development?\n(a) JavaScript\n(b) PHP\n(c) Ruby\n", "b")
    ]



def main():
    while True:
        print("Choisissez votre langue / Choose your language:")
        print("1. Français")
        print("2. English")
        choice = input("Votre choix / Your choice: ")

        if choice == '1':
            questions = create_questions_fr()
        elif choice == '2':
            questions = create_questions_en()
        else:
            print("Choix invalide / Invalid choice")
            continue

        score, total_questions = run_quiz(questions)

        while True:
            play_again = input("Voulez-vous continuer? (o/n): ")
            if play_again.lower() == 'o':
                break
            elif play_again.lower() == 'n':
                print("Au revoir!")
                return
            else:
                print("Veuillez entrer 'o' pour oui ou 'n' pour non.")

if __name__ == "__main__":
    main()
