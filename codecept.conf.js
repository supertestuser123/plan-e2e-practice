/** @type {CodeceptJS.MainConfig} */
exports.config = {
  tests: './tests/fe/*_test.js',
  output: './output',
  helpers: {
    Playwright: {
      show: true,
      browser: 'chromium'
    }
  },
  include: {
    I: './steps_file.js',
    prodPlan: "./framework/pages/ProductionPlan.js",
  },
  name: 'plan-e2e-practice'
}