import { DojoMailAppPage } from './app.po';

describe('dojo-mail-app App', () => {
  let page: DojoMailAppPage;

  beforeEach(() => {
    page = new DojoMailAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
