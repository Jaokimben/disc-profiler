// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Amélioration de l'expérience utilisateur pour le formulaire de questionnaire
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    
    radioButtons.forEach(function(radio) {
        radio.addEventListener('change', function() {
            // Trouver tous les labels dans le même groupe de questions
            const questionGroup = this.closest('.mb-4');
            const labels = questionGroup.querySelectorAll('.list-group-item');
            
            // Réinitialiser tous les styles
            labels.forEach(function(label) {
                label.classList.remove('active');
                label.style.backgroundColor = '';
                label.style.fontWeight = '';
            });
            
            // Appliquer le style au label sélectionné
            const selectedLabel = this.closest('.list-group-item');
            selectedLabel.classList.add('active');
            selectedLabel.style.backgroundColor = '#e9ecef';
            selectedLabel.style.fontWeight = 'bold';
            
            // Appliquer une couleur en fonction du profil DISC sélectionné
            if (this.value === 'D') {
                selectedLabel.style.borderLeft = '5px solid var(--disc-red)';
            } else if (this.value === 'I') {
                selectedLabel.style.borderLeft = '5px solid var(--disc-yellow)';
            } else if (this.value === 'S') {
                selectedLabel.style.borderLeft = '5px solid var(--disc-green)';
            } else if (this.value === 'C') {
                selectedLabel.style.borderLeft = '5px solid var(--disc-blue)';
            }
        });
    });
    
    // Animation pour les cartes de profil sur la page d'accueil
    const profileCards = document.querySelectorAll('.card');
    
    profileCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
            this.style.boxShadow = '0 8px 15px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
    
    // Vérification que tous les champs sont remplis avant soumission
    const questionnaireForm = document.querySelector('form');
    
    if (questionnaireForm) {
        questionnaireForm.addEventListener('submit', function(event) {
            const unansweredQuestions = [];
            
            // Vérifier chaque groupe de questions
            for (let i = 1; i <= 10; i++) {
                const questionName = 'q' + i;
                const answered = document.querySelector(`input[name="${questionName}"]:checked`);
                
                if (!answered) {
                    unansweredQuestions.push(i);
                }
            }
            
            // S'il y a des questions sans réponse
            if (unansweredQuestions.length > 0) {
                event.preventDefault();
                alert(`Veuillez répondre à toutes les questions. Questions non répondues : ${unansweredQuestions.join(', ')}`);
                
                // Mettre en évidence les questions non répondues
                unansweredQuestions.forEach(function(qNum) {
                    const questionGroup = document.querySelector(`[name="q${qNum}"]`).closest('.mb-4');
                    questionGroup.style.border = '2px solid #dc3545';
                    questionGroup.style.borderRadius = '5px';
                    questionGroup.style.padding = '10px';
                });
            }
        });
    }
    
    // Animation des barres de progression sur la page de résultats
    const progressBars = document.querySelectorAll('.progress-bar');
    
    if (progressBars.length > 0) {
        progressBars.forEach(function(bar) {
            const targetWidth = bar.style.width;
            bar.style.width = '0%';
            
            setTimeout(function() {
                bar.style.transition = 'width 1s ease-in-out';
                bar.style.width = targetWidth;
            }, 200);
        });
    }
});
