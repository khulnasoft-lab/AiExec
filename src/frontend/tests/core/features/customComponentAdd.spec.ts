import { expect, test } from "@playwright/test";
import { awaitBootstrapTest } from "../../utils/await-bootstrap-test";

test(
  "custom component code button should be pink when adding custom component",
  { tag: ["@release", "@components"] },

  async ({ page }) => {
    await awaitBootstrapTest(page);

    await page.waitForSelector('[data-testid="blank-flow"]', {
      timeout: 3000,
    });

    await page.getByTestId("blank-flow").click();

    await page.waitForSelector('[data-testid="zoom_out"]', {
      timeout: 3000,
    });

    await page.getByTestId("sidebar-custom-component-button").click();

    await expect(page.getByTestId("code-button-modal")).toBeVisible({
      timeout: 3000,
    });

    await expect(page.getByTestId("code-button-modal")).toHaveClass(
      /animate-pulse-pink/,
    );

    await page.getByTestId("code-button-modal").last().click();

    const waitTimeoutCode = `
# from aiexec.field_typing import Data
from aiexec.custom import Component
from aiexec.io import MessageTextInput, Output
from aiexec.schema import Data
from time import sleep
from aiexec.schema.message import Message

class CustomComponent(Component):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "https://docs.aiexec.org/components-custom-components"
    icon = "custom_components"
    name = "CustomComponent"

    inputs = [
        MessageTextInput(name="input_value", display_name="Input Value", value="Hello, World!"),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Message:
        data = Data(value=self.input_value)
        self.status = data
        sleep(60)
        return data`;

    await page.locator(".ace_content").click();
    await page.keyboard.press(`ControlOrMeta+A`);
    await page.locator("textarea").fill(waitTimeoutCode);

    await page.getByText("Check & Save").last().click();

    await expect(page.getByTestId("code-button-modal")).not.toHaveClass(
      /animate-pulse-pink/,
      { timeout: 3000 },
    );
  },
);
