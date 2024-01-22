const config = require('../../framework/config/config')
Feature('Расчет Производственного Плана')

Before(({ prodPlan }) => { 
  prodPlan.visit(config.base_url)
  prodPlan.checkIfOpen()
  prodPlan.fill_username(config.user.username)
  prodPlan.fill_password(config.user.password)
  prodPlan.submitForm()
  prodPlan.checkIfStageIsOpen()
  })

// Scenario('Проверка успешной авторизации', ({ I })=>{
//     I.seeInCurrentUrl('https://splan-stage.samoletgroup.ru/projects?limit=10&page=1');
// })

Scenario('Открытие страницы Производственного Плана',async({ I, prodPlan }) => {
    prodPlan.goToProductionPlanPage()
    prodPlan.uploadFiles()
    prodPlan.clickToCalculate()
    prodPlan.waitAndDownload()  
})
