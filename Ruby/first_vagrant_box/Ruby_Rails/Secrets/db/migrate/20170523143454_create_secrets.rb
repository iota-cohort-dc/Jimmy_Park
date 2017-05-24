class CreateSecrets < ActiveRecord::Migration
  def change
    create_table :secrets do |t|
      t.string :secret
      t.references :user

      t.timestamps null: false
    end
  end
end
