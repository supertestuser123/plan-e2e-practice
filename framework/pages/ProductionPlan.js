const { base_url } = require("../config/config");

const { I } = inject();

module.exports = {

  locators:{
    username: '[name=username]',
    password: '[name=password]',
    button: '[name=loginButton]',
    projects: {xpath: "//a[contains(@href,'projects') and contains(text(),'Проекты')]"},
    production_plan: {xpath: "//a[contains(@href,'production-plan') and contains(text(),'Производственный план')]"},
    calculate_button: '//button[@data-testid="tend-ui-button" and contains(text(), "Запустить перерасчет")]',
    successful_toast: '//span[text()="Выбранные файлы загружены"]', 
    download_button: '//div[@class="tend-ui-modal-content"]//button[text()="Скачать"]',
    modal_upload_window: '//*[text()="Перерасчет запущен"]',
    modal_download_window: '//div[@class="tend-ui-modal-title" and contains(text(), "Перерасчет завершен")]'


 },
  
  visit(){
  I.amOnPage(base_url)
  },

  checkIfOpen(){
    I.see('Вход в производственную систему Pro. Samolet');
  },
 
  fill_username(username){
    I.fillField(this.locators.username, username)
  },

  fill_password(password){
    I.fillField(this.locators.password, password)
  },

  submitForm(){
    I.click(this.locators.button)
  },

  checkIfStageIsOpen(){
    I.waitForElement(this.locators.projects, 30)
  },

  goToProductionPlanPage(){
    I.waitForElement(this.locators.production_plan, 30)
    I.click(this.locators.production_plan)
    I.waitForElement(this.locators.calculate_button)
  },

  async uploadFiles(){

  // Найти элемент input для выбора файлов
    const fileInputLocator = 'input[type="file"]';
    const fileInput = locate(fileInputLocator);

  // Загрузить файлы
    const files = [
      '/files/Стоп-лист.xlsx',
      '/files/Координаты_объектов.xlsx',
      '/files/Производственный_план.xlsx',
      '/files/Комплексные_подрядчики.xlsx',
      '/files/Пользовательский_конфиг.xlsx',
      '/files/Подрядчик_Предельная_площадь.xlsx',  
      '/files/Производственный_план_предыдущий_год.xlsx',
    ];

    for (const file of files) {
      I.attachFile(fileInput, file);
    
    }
    
    return Promise.resolve();
  },

  clickToCalculate(){
    I.waitForInvisible(this.locators.successful_toast, 3000)
    I.waitForElement(this.locators.calculate_button, 1000)
    I.click(this.locators.calculate_button)

  },

  waitAndDownload(){
    I.waitForElement(this.locators.modal_upload_window, 5000)
    I.waitForElement(this.locators.download_button,5000) 
    I.click(this.locators.download_button)
    
  },


}

