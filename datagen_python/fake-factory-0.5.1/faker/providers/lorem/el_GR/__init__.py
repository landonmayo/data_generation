# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as LoremProvider


class Provider(LoremProvider):
    common_words = (
        'άρα', 'ένα', 'ένας', 'έξι', 'έτσι', 'έχω', 'ήδη', 'ίδιο', 'αν', 'ανά',
        'από', 'ας', 'για', 'δε', 'δεν', 'δύο', 'εγώ', 'εδώ', 'εκτός', 'επί', 'θα',
        'κάτι', 'και', 'κι', 'μέχρι', 'μα', 'μας', 'με', 'μη', 'μην', 'μια', 'μιας',
        'μου', 'να', 'ναι', 'ο', 'οι', 'πάντα', 'πάντως', 'πιο', 'πλέον', 'ποια',
        'πολύ', 'που', 'πως', 'σαν', 'σας', 'σε', 'σου', 'στα', 'στη', 'στις',
        'στο', 'τα', 'τη', 'την', 'της', 'τι', 'τις', 'το', 'τον', 'του', 'τους',
        'των', 'ως', 'όσο', 'όταν', 'ότι', 'όχι'
    )

    word_list = common_words * 2 + (
        'άλγεβρα', 'άπειρα', 'άρα', 'άρθρων', 'άτομο', 'έγραψες', 'έλεγχος',
        'έξι', 'έρθει', 'έστειλε', 'έστελνε', 'έτοιμος', 'έτσι',
        'έχω', 'ήδη', 'ίδιο', 'αγοράζοντας', 'αθόρυβες', 'ακούσει', 'αλγόριθμου',
        'αναγκάζονται', 'ανακλύψεις', 'αναφέρονται', 'αναφορά',
        'ανεπιθύμητη', 'ανταγωνιστής', 'αντιλήφθηκαν', 'ανώδυνη', 'απίστευτα',
        'απαράδεκτη', 'απαραίτητο', 'απαρατήρητο', 'απλό', 'αποδείξεις',
        'αποθηκευτικού', 'αποκλειστικούς', 'απομόνωση', 'αποστηθίσει',
        'αποφάσισε', 'από', 'απόλαυσε', 'αρέσει', 'αρπάζεις', 'αρχεία',
        'ατόμου', 'αυτήν', 'αυτός', 'αφήσεις', 'βάζοντας', 'βαθμό',
        'βασανίζουν', 'βγήκε', 'βιαστικά', 'βιβλίο', 'βουτήξουν', 'βρίσκονται',
        'γέλασαν', 'γεγονός', 'γειτονιάς', 'γεύματος', 'για', 'γιαυτό',
        'γνωρίζουμε', 'γνωστή', 'γράψει', 'γραμμές', 'γραμμή', 'γραμμής',
        'γραφικά', 'δίνοντας', 'δε', 'δείξει', 'δεδομένων', 'δεν',
        'δημιουργήσεις', 'δημιουργείς', 'δημιουργια', 'διάβασε', 'διάσημα',
        'διαδίκτυο', 'διακοπή', 'διακοπής', 'διακόψουμε', 'διαπιστώνεις',
        'διασφαλίζεται', 'διαφήμιση', 'διαχειριστής', 'διευθυντές', 'διοικητικό',
        'διολισθήσεις', 'διορθώσει', 'διορθώσεις', 'δοκιμάσεις', 'δουλεύει',
        'δούλευε', 'δυστυχής', 'δυστυχώς', 'δωροδοκηθούν', 'δύο', 'είχαμε',
        'εγώ', 'εδώ', 'ειδικά', 'εικόνες', 'εκδόσεις', 'εκείνου', 'εκθέσεις',
        'εκτελέσει', 'εκτελέσεις', 'εκτελείται', 'εκτός', 'ελέγχου', 'εντολές',
        'εξακολουθεί', 'εξαρτάται', 'εξοργιστικά', 'επί', 'επενδυτής',
        'επεξεργασία', 'επιδιορθώσεις', 'επιδιόρθωση', 'επιστρέφουν',
        'επιχείριση', 'εργάστηκε', 'εργαζόμενοι', 'εργαζόμενων', 'εργαλείων',
        'εργασίας', 'εργοστασίου', 'ερωτήσεις', 'ερώτηση', 'εσωτερικών',
        'εταιρείες', 'ευκολότερο', 'εφαμοργής', 'εφαρμογή', 'εφαρμογής',
        'ζητήσεις', 'ημέρα', 'θέλεις', 'θέμα', 'θέματα', 'θυμάμαι',
        'ιδιαίτερα', 'κάνε', 'κάνεις', 'κάτι', 'και', 'καλύτερο', 'κανένας',
        'κανείς', 'κανόνα', 'καταλάθος', 'κειμένων', 'κι', 'κλπ', 'κοιτάζοντας',
        'κρατάει', 'κρατήσουν', 'κόλπα', 'κόψεις', 'κύκλο', 'κώδικάς', 'κώδικα',
        'λέει', 'λίγο', 'λαμβάνουν', 'λες', 'λετπά', 'λιγότερο', 'λοιπόν', 'μάθε',
        'μάλλον', 'μάτσο', 'μέγιστη', 'μέρος', 'μέσης', 'μέχρι', 'μαγικά',
        'μερικούς', 'μεταγλωτίσει', 'μεταγλωτιστής',
        'μεταφραστής', 'μετράει', 'μετρήσεις', 'μηχανής',
        'μπορούσες', 'μπουν', 'νέα', 'νέο', 'νέου', 'νέων', 'νιρβάνα', 'νόμιζες',
        'ξέχασε', 'ορίστε', 'πάντα', 'πάντως', 'πάρα', 'πάρεις', 'πήρε', 'παίξουν',
        'παίρνει', 'παίρνουν', 'πακέτων', 'παράγοντες', 'παράδειγμα',
        'παραγωγικής', 'παραδοτέου', 'παραδώσεις', 'παραπάνω', 'πεδία',
        'περίπου', 'περιβάλλον', 'περιβάλλοντος', 'περιεχόμενα', 'περιμένουν',
        'περισσότερες', 'περισσότερη', 'πες', 'πετάνε', 'πετάξαμε', 'πετούν',
        'πηγαίου', 'πιο', 'πλέον', 'ποια', 'πολύ', 'ποσοστό', 'που',
        'προβληματική', 'προγραμματιστές', 'προγραμματιστής', 'προκαλείς',
        'προκύπτουν', 'προσεκτικά', 'προσθέσει', 'προσλάμβανες', 'προσοχή',
        'προσπαθήσεις', 'προσπαθούν', 'προϊόντα', 'πρόσληψη', 'πρώτης', 'πρώτο',
        'πρώτοι', 'πόρτες', 'ροή', 'ρουτίνα', 'ρωτάει', 'ρωτήσει',
        'σίγουρος', 'σημαντικό', 'σημαντικός', 'σημεία',
        'σκεφτείς', 'σπίτι', 'στέλνοντάς', 'στήλες', 'σταματάς',
        'στραβά', 'συγγραφής', 'συγγραφείς',
        'συγκεντρωμένοι', 'συγχρόνως', 'συγχωνευτεί', 'συνάδελφος', 'συνέχεια',
        'συνεντεύξεις', 'συνεχώς', 'συνηθίζουν', 'σχεδιαστής', 'σωστά',
        'τέλειοι', 'τα', 'ταξινομεί', 'τεκμηριώνει', 'τελειώσει', 'τεσσαρών',
        'τοπικές', 'τρέξει', 'τρόπο', 'τρόποι', 'τύπου', 'τύπους', 'υπηρεσία',
        'υποψήφιο', 'υψηλότερη', 'υόρκη', 'φίλος', 'φαινόμενο', 'φακέλους',
        'φράση', 'χάος', 'χαμηλός', 'χαρακτηριστικό', 'χαρακτηριστικών',
        'χαρτιού', 'χειρότερα', 'χρειάζονται', 'χρησιμοποίησέ',
        'χρησιμοποιούνταν', 'χρησιμοποιούσες', 'χρησιμοποιώντας',
        'χρονοδιαγράμματα', 'χρονοδιαγράμματος', 'χρόνου', 'χώρου', 'ωραίο',
        'ύψος', 'ώρα',
    )
