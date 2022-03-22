

describe('TodayTix app', () => {
    beforeEach(() => {
     
      cy.visit('https://todaytix.com')
    })
    //Automate following scenario
    it('Home Page is Displayed', () => {
      //  Go to todaytix.com
      //  Select the location as New York
      cy.get('.jss31').click()
      cy.get('#mobile-locations-menu-item-8').contains("New York")
      cy.get('#mobile-locations-menu-item-8').click
      
    })
  
    it('Choose Movie', () => {
   
      //
      const newItem = 'Wicked'
      //cy.get('#NYC\ -\ New\ and\ Hot\ on\ TodayTix-item-1-link').click
      cy.get('.jss24 > .MuiSvgIcon-root').click

      cy.get('#topBarSearch').type("Wicked")
      cy.get('*[@id="searchBar"]/div/div').click
    })
  
    it('Validate Movie Page', () => {
      //  Select a show e.g. ‘Wicked’
      //  Validate show page displays
      cy.visit("https://www.todaytix.com/nyc/shows/1-wicked")
      const newItem = 'Wicked'
      cy.get('#product-h1').contains(newItem)
    })
  
    it('purchase Tickets', () => {
         //  Click on ‘Get Tickets’ and validate Calendar form displays
      //  Select a date and validate showTime form displays
        cy.visit("https://www.todaytix.com/nyc/shows/1-wicked")
        cy.get('#view-prices').click 
        cy.get('.jss171').contains("$99")
        
      })
    

    it('Validate Calendar', () => {
        //  Click on ‘Get Tickets’ and validate Calendar form displays
     //  Select a date and validate showTime form displays
       cy.visit("https://www.todaytix.com/nyc/shows/1-wicked/purchase")
       cy.get(':nth-child(1) > ._3lFWdo983S > ._3YvhbOXVDS > :nth-child(2) > :nth-child(2) > :nth-child(4) > :nth-child(4) > ._1DR_voUcS3').click
       cy.get('._6L78EmupXs').contains("7:00PM")
       cy
     })
    })
    

       //  Select from Price and validate section form displays
      //  Select a section and validate user details form displays with two payment options Google Pay and Credit Card
      //  Fill out the user form and click on credit card and validate credit card form displays
  
